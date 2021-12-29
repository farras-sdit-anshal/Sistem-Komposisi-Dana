import requests

"""
Documentation for retrieve from gravity forms

-> https://docs.gravityforms.com/rest-api-v2/#authentication-2


Gets entries associated with a specific forms.
https://localhost/wp-json/gf/v2/forms/185/entries

------------------------------------------------------------------------------------------------------------------------
OPTIONAL ARGUMENT
_field_ids – A comma separated list of fields to include in the response.
_labels – Enables the inclusion of field labels in the results. Use the value “1” to include labels.
paging – The paging criteria.
The paging encompasses the following:
        page_size – The number of results per page.
        current_page – The current page from which to pull details.
        offset – The offset to begin with.
search – The search criteria.
The search encompasses the following:
        field_filters – An array of filters to search by.
        key – The field ID.
        value – The value to search for.
        operator – The comparison operator to use.
sorting – The sorting criteria.
The sorting encompasses the following:
        key – The key by which to sort.
        direction – The direction. Either ASC or DESC.
        is_numeric – If the key is numeric.
------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------
SAMPLE USAGE
https://localhost/wp-json/gf/v2/forms/1/entries?_field_ids=1,6.1,6.2,6.3,date_created

https://localhost/wp-json/gf/v2/forms/1/entries?_labels=1

https://localhost/wp-json/gf/v2/forms/1/entries?paging[page_size]=20&paging[current_page]=2&paging[offset]=30

https://localhost/wp-json/gf/v2/forms/1/entries/?search={"field_filters": [{"key":2,"value":"test",
"operator":"contains"}]}

https://localhost/wp-json/gf/v2/forms/1/entries?sorting[key]=id&sorting[direction]=ASC&sorting[is_numeric]=true
------------------------------------------------------------------------------------------------------------------------

"""


def respone_gv_api():
    """
        https://localhost/wp-json/gf/v2/forms/185/entries
    """
    # rspn = requests.get('https://ypiiah.id/wp-json/gf/v2/forms/12/entries?search={"field_filters": [{'
    #                     '"key":"workflow_final_status","value":"Pending"}]}',
    #                     auth=('ck_854afcde0a232a8289120acc3b3a5725bc85f946',
    #                           'cs_5e3f0b4ba4bbffad8a40b6641b765c5b1dd2fdec'))

    rspn = requests.get('https://ypiiah.id/wp-json/gf/v2/forms/12/entries?paging[page_size]=50&search={'
                        '"field_filters": [{ '
                        '"key":"workflow_final_status","value":"Pending"}]}',
                        auth=('ck_007549c0f17fd8d7e5f9e1d86a87225045d0016c',
                              'cs_68caa6c38d5bd0cabf82fd2f58407236895629f5'))

    # auth = ('ck_854afcde0a232a8289120acc3b3a5725bc85f946',
    #         'cs_5e3f0b4ba4bbffad8a40b6641b765c5b1dd2fdec'))

    return rspn.json()
