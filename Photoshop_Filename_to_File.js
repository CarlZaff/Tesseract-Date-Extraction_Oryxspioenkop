// Save the original ruler units preference of the application
var originalRulerUnits = preferences.rulerUnits;

// Set the ruler units to percentages
preferences.rulerUnits = Units.PERCENT;

// Get a reference to the active document
var docRef = activeDocument;

// Add a new layer to the active document
var myLayerRef = docRef.artLayers.add();

// Add a second new layer to the active document
var myLayerRef2 = docRef.artLayers.add();

// Set the first layer to a text layer
myLayerRef.kind = LayerKind.TEXT;

// Set the name of the first layer to "Filename"
myLayerRef.name = "Filename";

// Set the second layer to a text layer
myLayerRef2.kind = LayerKind.TEXT;

// Set the name of the second layer to "Filename2"
myLayerRef2.name = "Filename2";

// Get a reference to the text item of the first layer
var myTextRef = myLayerRef.textItem;

// Get a reference to the text item of the second layer
var myTextRef2 = myLayerRef2.textItem;

// Set the font size of the first layer to a specific size
myTextRef.size = (72/docRef.resolution)*70;

// Set the font size of the second layer to the same size as the first layer
myTextRef2.size = myTextRef.size;

// Set the font of the first layer to "Calibri"
myTextRef.font = "Calibri";

// Create a new SolidColor object
var newColor = new SolidColor();

// Set the red component of the color to 0
newColor.rgb.red = 0;

// Set the green component of the color to 0
newColor.rgb.green = 0;

// Set the blue component of the color to 0
newColor.rgb.blue = 0;

// Set the color of the first layer to the newly created SolidColor object
myTextRef.color = newColor;

// Set the color of the second layer to the newly created SolidColor object
myTextRef2.color = newColor;

// Set the position of the first layer
myTextRef.position = new Array(50, 6.5);

// Set the position of the second layer
myTextRef2.position = new Array(50, 97.5);

// Get the position of the "." character in the name of the active document
var di = (docRef.name).indexOf(".");

// Extract the file name without the extension
var fname = (docRef.name).substr(0, di);

// Set the content of the first layer to the extracted file name
myTextRef.contents = fname;

// Set the content of the second layer to the extracted file name
myTextRef2.contents = fname;

// Restore the original ruler units preference of the application
preferences.rulerUnits = originalRulerUnits;
