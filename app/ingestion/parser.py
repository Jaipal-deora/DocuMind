from llama_index.core.node_parser import SentenceSplitter

def parse_documents(docs):
    parser = SentenceSplitter(
        chunk_size=512,
        chunk_overlap = 50
    )

    nodes = parser.get_nodes_from_documents(docs)

    for node in nodes:
        node.metadata.update(node.source_node.metadata)
        # node.metadata.update(node.ref_doc_id)
        
    return nodes 