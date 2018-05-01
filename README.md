# Automatic Semantic Search Engine for Suitable Standards

The Automatic Semantic Search Engine for Suitable Standards (ASSESS) is an open-source software technology to easily identify and obtain the recommemded industrial standards for a given search query, which could be a Statement Of Work (SOW), Performance Work Statement (PWS) or simply plain text.

ASSESS provides search analytics capabilities to:
1. Parse unstructured SOW and PWS documents in PDF, Word, and other document formatsi by leveraging Use Apache Tika.
2. Extract relevant features and textual and language and other content from those documents and make that information available for search.
3. Match up relevant Standards references and documents to SOW and PWS identified and parsed in step 1.
4. Provide a recommendation/ranking and algorithm for delivering these recommendations to PMs. Create a search index in ElasticSearch and Apache Solr for the recommendations.
5. Provide visual analytics over the index in step 5.
