```json
{
  response: {
    GET_STATS_DATA: {
      RESULT: {
        STATUS: {},
        ERROR_MSG: {},
        DATE: {}
      },
      PARAMETER: {
        LANG: {},
        STATS_DATA_ID: {},
        DATA_FORMAT: {},.
        START_POSITION: {},
        ...
      }
      STATISTICAL_DATA: {
        RESULT_INF: {
          TOTAL_NUMBER: {},
          FROM_NUMBER: {},
          TO_NUMBER: {},
          NEXT_KEY: {}
        },
        TALBE_INF: {
          @id
          STAT_NAME
          GOV_ORG
          STATISTICS_NAME
          TITLE
          CYCLE
          SURVEY_DATE
          OPEN_DATE
          SMALL_AREA
          COLLECT_AREA
          MAIN_CATEGORY
          SUB_CATEGORY
          OVERALL_TOTAL_NUMBER
          UPDATED_DATE
          STATISTICS_NAME_SPEC
          DESCRIPTION
          TITLE_SPEC
        },
        CLASS_INF: {
          CLASS_OBJ: {}
        },
        DATA_INF: {
          NOTE: "",
          VALUE: []
        }
      }
    }
  }
}
```