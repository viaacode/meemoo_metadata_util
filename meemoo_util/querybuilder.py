def generate_query(fields, multiselect_fields, filters={}):
    sq = "SELECT "
    sq += ', '.join(list(map(lambda f: "xpath('/VIAA/" + f +"/text()', xmldata::xml) AS " + f, fields)))
    sq += ', '
    sq += ','.join(list(map(lambda f: "xpath('/VIAA/" + f +"/*', xmldata::xml) AS " + f, multiselect_fields)))
    sq += ' FROM jobbd '

    if filters:
        sq += 'WHERE '
        if filters["batch_id"]:
            sq += 'batch_id = ' + str(filters["batch_id"])
    
    q = "SELECT "
    q += ', '.join(list(map(lambda f: f + "[1]::text AS " + f, fields)))
    q += ','
    q += ','.join(list(map(lambda f: f + "[1]::text AS " + f, multiselect_fields)))
    q += ' FROM (' + sq + ') y'
    
    return str(q)

FIELDS = ["CP", "CP_id", "dc_identifier_localid", "dc_title", "dcterms_created", "dcterms_issued"]
MULTISELECT_FIELDS = ["dc_identifier_localids", "dc_titles", "dc_rights_licenses", "dc_subjects"]

ge_query = generate_query(FIELDS, MULTISELECT_FIELDS, {"batch_id":  5})