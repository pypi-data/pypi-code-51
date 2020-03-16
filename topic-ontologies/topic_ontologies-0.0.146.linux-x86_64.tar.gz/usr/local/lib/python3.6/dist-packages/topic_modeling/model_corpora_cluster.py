import sys
sys.path.insert(0,"/home/yamenajjour/git/topic-ontologies/")

from pyspark.sql import SparkSession
import argument_esa_model.esa_all_terms
import argument_esa_model.esa_top_n_terms
import pickle
import codecs
from conf.configuration import *
set_cluster_mode()


spark = SparkSession.builder.appName('topic-ontologies').config('master','yarn').getOrCreate()
args_me = spark.read.format('csv').option('header','true').option('delimiter',',')
spark_context= spark.sparkContext

def dict_to_list(dictionary):
    vector  = []
    for key in sorted(dictionary):
        vector.append(dictionary[key])
    pickled = codecs.encode(pickle.dumps(vector), "base64").decode()
    return pickled

URI = spark_context._gateway.jvm.java.net.URI
Path = spark_context._gateway.jvm.org.apache.hadoop.fs.Path
FileSystem = spark_context._gateway.jvm.org.apache.hadoop.fs.FileSystem
FsPermission = spark_context._gateway.jvm.org.apache.hadoop.fs.permission.FsPermission
fs = FileSystem.get(URI("hdfs://betaweb020.medien.uni-weimar.de:8020"), spark_context._jsc.hadoopConfiguration())
fs.listStatus(Path('/user/befi8957'))

def project_arguments(topic_ontology,model,vocab_size,test):
    corpora = load_corpora_list()
    def project(argument):
        if test:
            return dict_to_list({'a':0.3,'b':0.3,'c':0.04})
        set_cluster_mode()
        path_word2vec_model = get_path_topic_model('word2vec','word2vec')
        path_word2vec_vocab = get_path_vocab('word2vec')
        if model == 'esa':
            path_topic_model = get_path_topic_model('ontology-'+topic_ontology,model)
            vector = argument_esa_model.esa_all_terms.model_topic(path_topic_model,path_word2vec_model,path_word2vec_vocab,'cos',argument)
            return dict_to_list(vector)
        else:
            path_corpus = get_path_source('ontology-' + topic_ontology)
            vector = argument_esa_model.esa_top_n_terms.model_topic(path_corpus,path_word2vec_model,path_word2vec_vocab,argument,vocab_size)
            return dict_to_list(vector)

    for corpus in corpora:
        granularity = get_granularity(corpus)
        if granularity == 'argument':
            path_arguments = get_path_preprocessed_arguments(corpus)
            path_argument_vectors= get_path_argument_vectors(corpus,topic_ontology,model).replace(".csv","")
            documents_df  = spark.read.format("csv").option("header", "true").option("delimiter", "|", ).option('quote', '"').load(path_arguments).na.drop()
            arguments = documents_df.select("argument").rdd.map(lambda r: r[0]).repartition(200)
            ids = (documents_df.select("argument-id").rdd.map(lambda r: r[0])).repartition(200)
            vectors = arguments.map(lambda argument:project(argument))
            ids_with_vectors=vectors.zip(ids)
            FileSystem.mkdirs(fs,Path(path_argument_vectors),FsPermission(77777))
            ids_with_vectors.saveAsTextFile(path_argument_vectors)
        else:
            path_documents = get_path_preprocessed_documents(corpus)
            path_documents_vectors= get_path_document_vectors(corpus,topic_ontology,model).replace(".csv","")
            documents_df  = spark.read.format("csv").option("header", "true").option("delimiter", "|", ).option('quote', '"').load(path_documents).na.drop()
            documents = documents_df.select("document").rdd.map(lambda r: r[0]).repartition(200)
            ids = (documents_df.select("document-id").rdd.map(lambda r: r[0])).repartition(200)
            vectors = documents.map(lambda document:project(document))
            ids_with_vectors=vectors.zip(ids)
            FileSystem.mkdirs(fs,Path(path_documents_vectors),FsPermission(77777))
            ids_with_vectors.saveAsTextFile(path_documents_vectors)



project_arguments('wikipedia','esa',1000,True)