---
UID: NA:
---

# Printerextension.h header

## -description

This header is used by print. For more information, see
- [print](../_print/index.md)

Printerextension.h contain these programming interfaces:


## Enumerations

| Title   | Description   |
| ---- |:---- |
| [tagPrintJobStatus enumeration](ne-printerextension-tagprintjobstatus.md) | This enumeration is a one-to-one mapping to the spooler flags suppled in the JOB_INFO_X structures. |
| [tagPrintSchemaConstrainedSetting enumeration](ne-printerextension-tagprintschemaconstrainedsetting.md) | The PrintSchemaConstrainedSetting enumeration specifies whether the Option is available based on the current device configuration. The constrained attribute appears only in a PrintCapabilities document. |
| [tagPrintSchemaParameterDataType enumeration](ne-printerextension-tagprintschemaparameterdatatype.md) | The PrintSchemaParameterDataType enumeration identifies the allowed data types for the Print Schema parameter. |
| [tagPrintSchemaSelectionType enumeration](ne-printerextension-tagprintschemaselectiontype.md) | The PrintSchemaSelectionType enumeration identifies how a Feature’s options should be selected. This property appears only in a PrintCapabilities document. |

## Interfaces

| Title   | Description   |
| ---- |:---- |
| [IPrintJob interface](nn-printerextension-iprintjob.md) | Contains properties that represent a print job. |
| [IPrintJob interface](nn-printerextension-iprintjob~r1.md) | Contains properties that represent a print job. |
| [IPrintJobCollection interface](nn-printerextension-iprintjobcollection.md) | This interfaces provides an enumeration of the jobs in the print queue. |
| [IPrintJobCollection interface](nn-printerextension-iprintjobcollection~r1.md) | This interfaces provides an enumeration of the jobs in the print queue. |
| [IPrintSchemaAsyncOperation interface](nn-printerextension-iprintschemaasyncoperation.md) | Represents an asynchronous operation context for validation, merge or commit operations. |
| [IPrintSchemaAsyncOperation interface](nn-printerextension-iprintschemaasyncoperation~r1.md) | Represents an asynchronous operation context for validation, merge or commit operations. |
| [IPrintSchemaAsyncOperationEvent interface](nn-printerextension-iprintschemaasyncoperationevent.md) | Exposes a validation, merge, or commit completion event delegate. |
| [IPrintSchemaAsyncOperationEvent interface](nn-printerextension-iprintschemaasyncoperationevent~r1.md) | Exposes a validation, merge, or commit completion event delegate. |
| [IPrintSchemaCapabilities interface](nn-printerextension-iprintschemacapabilities.md) | Provides the primary method to access PrintCapabilities. |
| [IPrintSchemaCapabilities interface](nn-printerextension-iprintschemacapabilities~r1.md) | Provides the primary method to access PrintCapabilities. |
| [IPrintSchemaCapabilities2 interface](nn-printerextension-iprintschemacapabilities2.md) | The IPrintSchemaCapabilities2 interface represents an extension to the IPrintSchemaCapabilities object, which provides wrapper methods over a print capabilities document. |
| [IPrintSchemaCapabilities2 interface](nn-printerextension-iprintschemacapabilities2~r1.md) | The IPrintSchemaCapabilities2 interface represents an extension to the IPrintSchemaCapabilities object, which provides wrapper methods over a print capabilities document. |
| [IPrintSchemaDisplayableElement interface](nn-printerextension-iprintschemadisplayableelement.md) | Provides the displayable string for a PrintCapabilites PrintSchema element. |
| [IPrintSchemaDisplayableElement interface](nn-printerextension-iprintschemadisplayableelement~r1.md) | Provides the displayable string for a PrintCapabilites PrintSchema element. |
| [IPrintSchemaElement interface](nn-printerextension-iprintschemaelement.md) | Provides access to the underlying XML node and &#0034;name&#0034; attribute information for a Print Schema element. |
| [IPrintSchemaElement interface](nn-printerextension-iprintschemaelement~r1.md) | Provides access to the underlying XML node and &#0034;name&#0034; attribute information for a Print Schema element. |
| [IPrintSchemaFeature interface](nn-printerextension-iprintschemafeature.md) | Exposes a Print Schema Feature element. |
| [IPrintSchemaFeature interface](nn-printerextension-iprintschemafeature~r1.md) | Exposes a Print Schema Feature element. |
| [IPrintSchemaNUpOption interface](nn-printerextension-iprintschemanupoption.md) | Exposes a Print Schema NUp Option element. |
| [IPrintSchemaNUpOption interface](nn-printerextension-iprintschemanupoption~r1.md) | Exposes a Print Schema NUp Option element. |
| [IPrintSchemaOption interface](nn-printerextension-iprintschemaoption.md) | Exposes a Print Schema Option object. |
| [IPrintSchemaOption interface](nn-printerextension-iprintschemaoption~r1.md) | Exposes a Print Schema Option object. |
| [IPrintSchemaOptionCollection interface](nn-printerextension-iprintschemaoptioncollection.md) | Exposes a collection of IPrintSchemaOption objects. |
| [IPrintSchemaOptionCollection interface](nn-printerextension-iprintschemaoptioncollection~r1.md) | Exposes a collection of IPrintSchemaOption objects. |
| [IPrintSchemaPageImageableSize interface](nn-printerextension-iprintschemapageimageablesize.md) | Exposes the PageImageableSize property of PrintCapabilities. The properties of this interface map directly to those in the PageImageableSize property of PrintCapabilities. |
| [IPrintSchemaPageImageableSize interface](nn-printerextension-iprintschemapageimageablesize~r1.md) | Exposes the PageImageableSize property of PrintCapabilities. The properties of this interface map directly to those in the PageImageableSize property of PrintCapabilities. |
| [IPrintSchemaPageMediaSizeOption interface](nn-printerextension-iprintschemapagemediasizeoption.md) | Exposes a Print Schema PageMediaSize Option element. |
| [IPrintSchemaPageMediaSizeOption interface](nn-printerextension-iprintschemapagemediasizeoption~r1.md) | Exposes a Print Schema PageMediaSize Option element. |
| [IPrintSchemaParameterDefinition interface](nn-printerextension-iprintschemaparameterdefinition.md) | The IPrintSchemaParameterDefinition interface represents a parameter definition, as defined in the Print Schema Specification. |
| [IPrintSchemaParameterDefinition interface](nn-printerextension-iprintschemaparameterdefinition~r1.md) | The IPrintSchemaParameterDefinition interface represents a parameter definition, as defined in the Print Schema Specification. |
| [IPrintSchemaParameterInitializer interface](nn-printerextension-iprintschemaparameterinitializer.md) | The IPrintSchemaParameterInitializer interface represents a parameter initialization value, as defined in the print schema specification. |
| [IPrintSchemaParameterInitializer interface](nn-printerextension-iprintschemaparameterinitializer~r1.md) | The IPrintSchemaParameterInitializer interface represents a parameter initialization value, as defined in the print schema specification. |
| [IPrintSchemaTicket interface](nn-printerextension-iprintschematicket.md) | Provides the primary method to access and validate a PrintTicket. |
| [IPrintSchemaTicket interface](nn-printerextension-iprintschematicket~r1.md) | Provides the primary method to access and validate a PrintTicket. |
| [IPrintSchemaTicket2 interface](nn-printerextension-iprintschematicket2.md) | The IPrintSchemaTicket2 interface is an extension to the IPrintSchemaTicket interface, which provides wrapper methods over a print ticket document. |
| [IPrintSchemaTicket2 interface](nn-printerextension-iprintschematicket2~r1.md) | The IPrintSchemaTicket2 interface is an extension to the IPrintSchemaTicket interface, which provides wrapper methods over a print ticket document. |
| [IPrinterBidiSetRequestCallback interface](nn-printerextension-iprinterbidisetrequestcallback.md) | Describes the signature of the callback object that receives the Bidi response. |
| [IPrinterBidiSetRequestCallback interface](nn-printerextension-iprinterbidisetrequestcallback~r1.md) | Describes the signature of the callback object that receives the Bidi response. |
| [IPrinterExtensionAsyncOperation interface](nn-printerextension-iprinterextensionasyncoperation.md) | Provides the context associated with an asynchronous operation. |
| [IPrinterExtensionAsyncOperation interface](nn-printerextension-iprinterextensionasyncoperation~r1.md) | Provides the context associated with an asynchronous operation. |
| [IPrinterExtensionContext interface](nn-printerextension-iprinterextensioncontext.md) | Represents the context for the activation of a UWP device app for printers. |
| [IPrinterExtensionContext interface](nn-printerextension-iprinterextensioncontext~r1.md) | Represents the context for the activation of a UWP device app for printers. |
| [IPrinterExtensionContextCollection interface](nn-printerextension-iprinterextensioncontextcollection.md) | Exposes a collection of IPrinterExtensionContext objects. |
| [IPrinterExtensionContextCollection interface](nn-printerextension-iprinterextensioncontextcollection~r1.md) | Exposes a collection of IPrinterExtensionContext objects. |
| [IPrinterExtensionEventArgs interface](nn-printerextension-iprinterextensioneventargs.md) | Represents the context for the desktop printer extension activation. |
| [IPrinterExtensionEventArgs interface](nn-printerextension-iprinterextensioneventargs~r1.md) | Represents the context for the desktop printer extension activation. |
| [IPrinterExtensionRequest interface](nn-printerextension-iprinterextensionrequest.md) | Completes the given extension event with either a cancellation or success. |
| [IPrinterExtensionRequest interface](nn-printerextension-iprinterextensionrequest~r1.md) | Completes the given extension event with either a cancellation or success. |
| [IPrinterPropertyBag interface](nn-printerextension-iprinterpropertybag.md) | Provides strongly-typed get and set methods. |
| [IPrinterPropertyBag interface](nn-printerextension-iprinterpropertybag~r1.md) | Provides strongly-typed get and set methods. |
| [IPrinterQueue interface](nn-printerextension-iprinterqueue.md) | Represents a single printer queue. |
| [IPrinterQueue interface](nn-printerextension-iprinterqueue~r1.md) | Represents a single printer queue. |
| [IPrinterQueue2 interface](nn-printerextension-iprinterqueue2.md) | Represents a single printer queue. |
| [IPrinterQueue2 interface](nn-printerextension-iprinterqueue2~r1.md) | Represents a single printer queue. |
| [IPrinterQueueEvent interface](nn-printerextension-iprinterqueueevent.md) | Provides the event delegate for printer queue events. |
| [IPrinterQueueEvent interface](nn-printerextension-iprinterqueueevent~r1.md) | Provides the event delegate for printer queue events. |
| [IPrinterQueueView interface](nn-printerextension-iprinterqueueview.md) | Provides a way to change the range of print jobs being monitored. |
| [IPrinterQueueView interface](nn-printerextension-iprinterqueueview~r1.md) | Provides a way to change the range of print jobs being monitored. |
| [IPrinterQueueViewEvent interface](nn-printerextension-iprinterqueueviewevent.md) | Provides the signature of the event handler. |
| [IPrinterQueueViewEvent interface](nn-printerextension-iprinterqueueviewevent~r1.md) | Provides the signature of the event handler. |
| [IPrinterScriptContext interface](nn-printerextension-iprinterscriptcontext.md) | Passed to all third-party constraints JavaScript functions, and provides access to relevant objects. |
| [IPrinterScriptContext interface](nn-printerextension-iprinterscriptcontext~r1.md) | Passed to all third-party constraints JavaScript functions, and provides access to relevant objects. |
| [IPrinterScriptablePropertyBag interface](nn-printerextension-iprinterscriptablepropertybag.md) | The IPrinterScriptablePropertyBag interface is the property bag interface passed to script clients. |
| [IPrinterScriptablePropertyBag interface](nn-printerextension-iprinterscriptablepropertybag~r1.md) | The IPrinterScriptablePropertyBag interface is the property bag interface passed to script clients. |
| [IPrinterScriptablePropertyBag2 interface](nn-printerextension-iprinterscriptablepropertybag2.md) | . |
| [IPrinterScriptablePropertyBag2 interface](nn-printerextension-iprinterscriptablepropertybag2~r1.md) | . |
| [IPrinterScriptableStream interface](nn-printerextension-iprinterscriptablestream.md) | The IPrinterScriptableStream interface builds on IPrinterScriptableSequentialStream and adds IStream-like semantics. |
| [IPrinterScriptableStream interface](nn-printerextension-iprinterscriptablestream~r1.md) | The IPrinterScriptableStream interface builds on IPrinterScriptableSequentialStream and adds IStream-like semantics. |
