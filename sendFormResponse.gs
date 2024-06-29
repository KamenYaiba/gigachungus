function sendFormResponse() {
  var wb = SpreadsheetApp.getActiveSpreadsheet();
  var sh = wb.getSheetByName("FR");
  if (sh) {
    var lastRow = sh.getLastRow();
    var lastColumn = sh.getLastColumn();
    var range = sh.getRange(lastRow, 2, 1, lastColumn);
    var displayValues = range.getDisplayValues();   
    var data = displayValues[0];

    

    var url = 'https://ahmadammarjr.pythonanywhere.com/reportreq';
    var next_sem_lost_points = '0';
    if (data[8].trim() != '') next_sem_lost_points = data[8].trim();
    var payload = {
      'key': SECRET,
      'repid': data[0].trim(),
      'points': data[1].trim(),
      'registered_hours': data[2].trim(),
      'passed_hours': data[3].trim(),
      'semester': data[4].trim(),
      'college': data[5].substring(0, data[5].indexOf('(')).trim().toLowerCase(),
      'sem_GPA': data[6].trim(),
      'next_sem_hours': data[7].trim(),
      'next_sem_lost_points': next_sem_lost_points

    };
    var setup = {
      'method': 'POST',
      'contentType': 'application/json',
      'payload': JSON.stringify(payload)
    };

    try{
      var response = UrlFetchApp.fetch(url, setup);
      Logger.log(response);
    }

    catch(e){
      Logger.log(e.message);
    }
    
  } 
}