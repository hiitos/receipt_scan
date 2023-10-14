from google.cloud import documentai_v1 as documentai
import config
import json
 
def process_document(project_id: str, location: str,
                     processor_id: str, file_path: str,
                     mime_type: str) -> documentai.Document:
    """
    Processes a document using the Document AI API.
    """
 
    # Instantiates a client
    documentai_client = documentai.DocumentProcessorServiceClient()
 
    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    # You must create new processors in the Cloud Console first
    resource_name = documentai_client.processor_path(
        project_id, location, processor_id)
 
    # Read the file into memory
    with open(file_path, "rb") as image:
        image_content = image.read()
 
        # Load Binary Data into Document AI RawDocument Object
        raw_document = documentai.RawDocument(
            content=image_content, mime_type=mime_type)
 
        # Configure the process request
        request = documentai.ProcessRequest(
            name=resource_name, raw_document=raw_document)
 
        # Use the Document AI client to process the sample form
        result = documentai_client.process_document(request=request)
 
        return result.document

def create_json_from_response(document):
    json_data = {}
    for entity in document.entities:
        print("---------")
        print(entity)
        print("---------")
        # break
        entity_type = entity.type_
        mention_text = entity.mention_text
        if entity.normalized_value:
            normalized_value = entity.normalized_value.text
        else:
            normalized_value = None
        # print(normalized_value)
        
        if entity_type not in json_data:
            json_data[entity_type] = {}
        
        if mention_text and normalized_value:
            json_data[entity_type][mention_text] = normalized_value
        elif mention_text:
            json_data[entity_type][mention_text] = None
        elif normalized_value:
            json_data[entity_type]["value"] = normalized_value
    
    return json_data

def main():
    """
    Run the codelab.
    """
    project_id = config.project_id
    location = config.location
    processor_id = config.processor_id
    file_path = config.file_path
    extension = file_path.split(".")[-1]

    # ファイルパスで分岐
    if extension == 'jpg':
        mime_type = 'image/jpeg'
    elif extension == 'pdf':
        mime_type = 'application/pdf'
    else:
        raise "Error"

    # Refer to https://cloud.google.com/document-ai/docs/processors-list for the supported file types
 
    document = process_document(project_id=project_id, location=location,
                                processor_id=processor_id, file_path=file_path,
                                mime_type=mime_type)
    # print(f"Text: {document.entities}")
    results = create_json_from_response(document)
    print("Document processing complete.")
    # print(document)
    print(results)

    # 保存するJSONファイルのパスを指定
    # output_file_path = 'output.json'
    # # resultsをJSONファイルに保存
    # with open(output_file_path, 'w', encoding='utf-8') as json_file:
    #     json.dump(results, json_file, ensure_ascii=False, indent=4)
    # print(f'Results saved to {output_file_path}')

    return results
 
if __name__ == "__main__":
    main()