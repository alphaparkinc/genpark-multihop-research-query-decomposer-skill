from client import MultihopResearchQueryDecomposerClient

def main():
    client = MultihopResearchQueryDecomposerClient()
    res = client.decompose_research_query()
    print('Query Decomposer: ' + res['decomposition_id'] + ' (' + str(len(res['sub_queries_generated'])) + ' sub-queries)')
    print('Waves: ' + str(res['synthesis_dag_waves_count']) + ' | Plan URL: ' + res['query_plan_url'])

if __name__ == '__main__':
    main()
