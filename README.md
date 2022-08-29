# world-fishing-api

this is hosted on "https://world-fish-api.herokuapp.com/"


route: "https://world-fish-api.herokuapp.com/findspecies/?specieskey={searchterm}", GET

    {searchterm: salmon, tuna, etc}



route: "https://world-fish-api.herokuapp.com/specienumbers", POST
  
    body:
      {
      "Code": "SAL",
      "Name": "Atlantic salmon",
      "Scientific Name": "Salmo salar"
      }
