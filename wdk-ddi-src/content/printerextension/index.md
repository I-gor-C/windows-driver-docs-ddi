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

## Methods

| Title   | Description   |
| ---- |:---- |
| [IPrintJob::RequestCancel method](nf-printerextension-iprintjob-requestcancel.md) | Requests the cancellation of a print job. |
| [IPrintJobCollection::GetAt method](nf-printerextension-iprintjobcollection-getat.md) | Gets a pointer to an IPrintJob object. |
| [IPrintSchemaAsyncOperation::Cancel method](nf-printerextension-iprintschemaasyncoperation-cancel.md) | Cancels the asynchronous PrintSchema operation. |
| [IPrintSchemaAsyncOperation::Start method](nf-printerextension-iprintschemaasyncoperation-start.md) | Starts the asynchronous PrintSchema operation. |
| [IPrintSchemaAsyncOperationEvent::Completed method](nf-printerextension-iprintschemaasyncoperationevent-completed.md) | Is called when asynchronous PrintSchema operation that is represented by an IPrintSchemaAsyncOperation context is completed. |
| [IPrintSchemaCapabilities2::GetParameterDefinition method](nf-printerextension-iprintschemacapabilities2-getparameterdefinition.md) | The GetParameterDefinition method retrieves the IPrintSchemaParameterDefinition object, and it represents the &lt;psf |
| [IPrintSchemaCapabilities::GetFeature method](nf-printerextension-iprintschemacapabilities-getfeature.md) | Gets a named feature from the PrintCapabilities, by name and full namespace URI. |
| [IPrintSchemaCapabilities::GetFeatureByKeyName method](nf-printerextension-iprintschemacapabilities-getfeaturebykeyname.md) | Gets a feature from the PrintCapabilities based on a given key name. |
| [IPrintSchemaCapabilities::GetOptions method](nf-printerextension-iprintschemacapabilities-getoptions.md) | Gets all the options of a feature. |
| [IPrintSchemaCapabilities::GetSelectedOptionInPrintTicket method](nf-printerextension-iprintschemacapabilities-getselectedoptioninprintticket.md) | Gets the selected option for a feature in IPrintSchemaTicket. |
| [IPrintSchemaFeature::GetOption method](nf-printerextension-iprintschemafeature-getoption.md) | Gets the option with the given name. |
| [IPrintSchemaOption::GetPropertyValue method](nf-printerextension-iprintschemaoption-getpropertyvalue.md) | Gets the XML node for the &#0034;value&#0034; child element of a &#0034;Property&#0034; or a &#0034;ScoredProperty&#0034; element with the given name. |
| [IPrintSchemaOptionCollection::GetAt method](nf-printerextension-iprintschemaoptioncollection-getat.md) | Gets a pointer to an IPrintSchemaOption object. |
| [IPrintSchemaTicket2::GetParameterInitializer method](nf-printerextension-iprintschematicket2-getparameterinitializer.md) | The GetParameterInitializer method retrieves the IPrintSchemaParameterInitializer object, and it represents the &lt;psf |
| [IPrintSchemaTicket::CommitAsync method](nf-printerextension-iprintschematicket-commitasync.md) | Gets an asynchronous PrintTicket commit operation context. |
| [IPrintSchemaTicket::GetCapabilities method](nf-printerextension-iprintschematicket-getcapabilities.md) | Gets an IPrintSchemaCapabilities object that represents the printer capabilities based on the current settings of this IPrintSchemaTicket object. |
| [IPrintSchemaTicket::GetFeature method](nf-printerextension-iprintschematicket-getfeature.md) | Gets a named feature from the PrintTicket, by name and full namespace URI. |
| [IPrintSchemaTicket::GetFeatureByKeyName method](nf-printerextension-iprintschematicket-getfeaturebykeyname.md) | Gets a feature from the PrintTicket based on the specified key name. |
| [IPrintSchemaTicket::NotifyXmlChanged method](nf-printerextension-iprintschematicket-notifyxmlchanged.md) | Notifies the print system that the XML DOM object has changed. |
| [IPrintSchemaTicket::ValidateAsync method](nf-printerextension-iprintschematicket-validateasync.md) | Gets an asynchronous PrintTicket validation operation context. |
| [IPrinterBidiSetRequestCallback::Completed method](nf-printerextension-iprinterbidisetrequestcallback-completed.md) | Invoked when the Bidi “Set”” operation is completed. |
| [IPrinterExtensionAsyncOperation::Cancel method](nf-printerextension-iprinterextensionasyncoperation-cancel.md) | Cancels the asynchronous operation. |
| [IPrinterExtensionContextCollection::GetAt method](nf-printerextension-iprinterextensioncontextcollection-getat.md) | Gets a pointer to an IPrinterExtensionContext object. |
| [IPrinterExtensionEvent::OnDriverEvent method](nf-printerextension-iprinterextensionevent-ondriverevent.md) | Called when a driver event occurs. |
| [IPrinterExtensionEvent::OnPrinterQueuesEnumerated method](nf-printerextension-iprinterextensionevent-onprinterqueuesenumerated.md) | Called when printer queues are enumerated. |
| [IPrinterExtensionManager::DisableEvents method](nf-printerextension-iprinterextensionmanager-disableevents.md) | Disallows events to be generated. |
| [IPrinterExtensionManager::EnableEvents method](nf-printerextension-iprinterextensionmanager-enableevents.md) | The EnableEvents method allows events to be generated for the specified printer driver until DisableEvents is called. |
| [IPrinterExtensionRequest::Cancel method](nf-printerextension-iprinterextensionrequest-cancel.md) | Completes the extension event with a cancellation. |
| [IPrinterExtensionRequest::Complete method](nf-printerextension-iprinterextensionrequest-complete.md) | Completes the extension event. |
| [IPrinterPropertyBag::GetBool method](nf-printerextension-iprinterpropertybag-getbool.md) | Reads a specified boolean property. |
| [IPrinterPropertyBag::GetBytes method](nf-printerextension-iprinterpropertybag-getbytes.md) | Reads a byte array property. |
| [IPrinterPropertyBag::GetInt32 method](nf-printerextension-iprinterpropertybag-getint32.md) | Reads an integer property. |
| [IPrinterPropertyBag::GetReadStream method](nf-printerextension-iprinterpropertybag-getreadstream.md) | Gets a stream in order to read from a stream property. |
| [IPrinterPropertyBag::GetString method](nf-printerextension-iprinterpropertybag-getstring.md) | Reads a string property. |
| [IPrinterPropertyBag::GetWriteStream method](nf-printerextension-iprinterpropertybag-getwritestream.md) | Gets a stream in order to write a stream property. |
| [IPrinterPropertyBag::SetBool method](nf-printerextension-iprinterpropertybag-setbool.md) | Writes a specified boolean property value. |
| [IPrinterPropertyBag::SetBytes method](nf-printerextension-iprinterpropertybag-setbytes.md) | Writes a byte array property. |
| [IPrinterPropertyBag::SetInt32 method](nf-printerextension-iprinterpropertybag-setint32.md) | Writes an integer property. |
| [IPrinterPropertyBag::SetString method](nf-printerextension-iprinterpropertybag-setstring.md) | Writes a string property. |
| [IPrinterQueue2::GetPrinterQueueView method](nf-printerextension-iprinterqueue2-getprinterqueueview.md) | Retrieves an IPrinterQueueView object, and initializes the object with the range of jobs to be monitored. |
| [IPrinterQueue2::SendBidiSetRequestAsync method](nf-printerextension-iprinterqueue2-sendbidisetrequestasync.md) | Uses an XML string value to send a Bidi Set request as an asynchronous operation. |
| [IPrinterQueue::GetProperties method](nf-printerextension-iprinterqueue-getproperties.md) | Gets the properties in the property bag for the queue. |
| [IPrinterQueue::SendBidiQuery method](nf-printerextension-iprinterqueue-sendbidiquery.md) | Performs an asynchronous refresh operation with the specified query, and invokes the IPrinterQueueEvent |
| [IPrinterQueueEvent::OnBidiResponseReceived method](nf-printerextension-iprinterqueueevent-onbidiresponsereceived.md) | Called when a bidi response is received. |
| [IPrinterQueueView::SetViewRange method](nf-printerextension-iprinterqueueview-setviewrange.md) | Sets the range of print jobs being monitored. |
| [IPrinterQueueViewEvent::OnChanged method](nf-printerextension-iprinterqueueviewevent-onchanged.md) | Provides an IPrintJobCollection object that provides a snapshot of a range of print jobs in the queue. |
| [IPrinterScriptablePropertyBag2::GetReadStreamAsXML method](nf-printerextension-iprinterscriptablepropertybag2-getreadstreamasxml.md) | . |
| [IPrinterScriptablePropertyBag::GetBool method](nf-printerextension-iprinterscriptablepropertybag-getbool.md) | Gets a specified boolean property. |
| [IPrinterScriptablePropertyBag::GetBytes method](nf-printerextension-iprinterscriptablepropertybag-getbytes.md) | Gets a byte array property. |
| [IPrinterScriptablePropertyBag::GetInt32 method](nf-printerextension-iprinterscriptablepropertybag-getint32.md) | Gets an integer property. |
| [IPrinterScriptablePropertyBag::GetReadStream method](nf-printerextension-iprinterscriptablepropertybag-getreadstream.md) | Gets a read stream and uses it to read from a property. |
| [IPrinterScriptablePropertyBag::GetString method](nf-printerextension-iprinterscriptablepropertybag-getstring.md) | Gets a string property. |
| [IPrinterScriptablePropertyBag::GetWriteStream method](nf-printerextension-iprinterscriptablepropertybag-getwritestream.md) | Gets a stream and uses it to write to a stream property. |
| [IPrinterScriptablePropertyBag::SetBool method](nf-printerextension-iprinterscriptablepropertybag-setbool.md) | Writes a specified boolean property value. |
| [IPrinterScriptablePropertyBag::SetBytes method](nf-printerextension-iprinterscriptablepropertybag-setbytes.md) | Writes a byte array property. |
| [IPrinterScriptablePropertyBag::SetInt32 method](nf-printerextension-iprinterscriptablepropertybag-setint32.md) | Writes an integer property. |
| [IPrinterScriptablePropertyBag::SetString method](nf-printerextension-iprinterscriptablepropertybag-setstring.md) | Writes a string property. |
| [IPrinterScriptableSequentialStream::Read method](nf-printerextension-iprinterscriptablesequentialstream-read.md) | The Read method reads bytes from the stream and returns them as a JavaScript array. |
| [IPrinterScriptableSequentialStream::Write method](nf-printerextension-iprinterscriptablesequentialstream-write.md) | The Write method writes the provided JavaScript array to the stream and returns the number of bytes written. |
| [IPrinterScriptableStream::Commit method](nf-printerextension-iprinterscriptablestream-commit.md) | Commits the operation. |
| [IPrinterScriptableStream::Seek method](nf-printerextension-iprinterscriptablestream-seek.md) | Sets the seek pointer. |
| [IPrinterScriptableStream::SetSize method](nf-printerextension-iprinterscriptablestream-setsize.md) | Sets the size of the scriptable stream, in bytes. |
