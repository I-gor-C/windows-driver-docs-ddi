---
UID: NA:filterpipeline
ms.assetid: 434b4bef-ac82-3eee-8cc8-8fbfd4bad71c
ms.author: windowsdriverdev
ms.date: 03/13/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# Filterpipeline.h header



This header is used by print. For more information, see
- [print](../_print/index.md)

Filterpipeline.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [DrvPopulateFilterServices function](nf-filterpipeline-drvpopulatefilterservices.md) | The DrvPopulateFilterServices function is called by the XPSDrv filter pipeline manager to allow the service provider to instantiate filter service objects in the filter pipeline property bag specified by the pPropertyBag parameter. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [__MIDL___MIDL_itf_filterpipeline_0000_0000_0001 enumeration](ne-filterpipeline-__midl___midl_itf_filterpipeline_0000_0000_0001.md) | The ExpsCompressionOptions enumeration describes compression options for an XPS part. |
| [__MIDL___MIDL_itf_filterpipeline_0000_0000_0002 enumeration](ne-filterpipeline-__midl___midl_itf_filterpipeline_0000_0000_0002.md) | The EXpsFontOptions enumeration describes the font options for an XPS part. |
| [__MIDL___MIDL_itf_filterpipeline_0000_0000_0003 enumeration](ne-filterpipeline-__midl___midl_itf_filterpipeline_0000_0000_0003.md) | The EXpsJobConsumption enumeration describes job consumption updates. |
| [__MIDL___MIDL_itf_filterpipeline_0000_0000_0004 enumeration](ne-filterpipeline-__midl___midl_itf_filterpipeline_0000_0000_0004.md) | "." |

## Interfaces

| Title   | Description   |
| ---- |:---- |
| [IFixedDocument interface](nn-filterpipeline-ifixeddocument.md) | The IFixedDocument interface represents a fixed document for an XPS document sequence. |
| [IFixedDocumentSequence interface](nn-filterpipeline-ifixeddocumentsequence.md) | The IFixedDocumentSequence interface represents the fixed document sequence for an XPS document. |
| [IFixedPage interface](nn-filterpipeline-ifixedpage.md) | A filter uses the IFixedPage interface to work with fixed pages in an XPS document. |
| [IInterFilterCommunicator interface](nn-filterpipeline-iinterfiltercommunicator.md) | The IInterFilterCommunicator interface is implemented in an object that resides in the PrintFilterPipelineSvc service and is made available to filters through methods in the IPrintPipelineFilter interface. |
| [IPartBase interface](nn-filterpipeline-ipartbase.md) | The IPartBase interface is a common base for document part interfaces. |
| [IPartColorProfile interface](nn-filterpipeline-ipartcolorprofile.md) | The IPartColorProfile interface is the abstraction for an XPS color profile. |
| [IPartDiscardControl interface](nn-filterpipeline-ipartdiscardcontrol.md) | The filter pipeline supports the discard control. |
| [IPartFont interface](nn-filterpipeline-ipartfont.md) | The IPartFont interface is the abstraction for fonts in a part. |
| [IPartFont2 interface](nn-filterpipeline-ipartfont2.md) | "." |
| [IPartImage interface](nn-filterpipeline-ipartimage.md) | The IPartImage interface is the abstraction for images in an XPS document. |
| [IPartPrintTicket interface](nn-filterpipeline-ipartprintticket.md) | The IPartPrintTicket interface is the abstraction for a print ticket in an XPS document. |
| [IPartResourceDictionary interface](nn-filterpipeline-ipartresourcedictionary.md) | The IPartResourceDictionary interface is the abstraction for an XPS resource dictionary. |
| [IPartThumbnail interface](nn-filterpipeline-ipartthumbnail.md) | The IPartThumbnail interface is an abstraction for thumbnails in an XPS document. |
| [IPrintClassObjectFactory interface](nn-filterpipeline-iprintclassobjectfactory.md) | TheIPrintClassObjectFactory interface creates print filter-related interfaces. |
| [IPrintPipelineFilter interface](nn-filterpipeline-iprintpipelinefilter.md) | The methods in the IPrintPipelineFilter interface are called for initialization and shutdown. A filter must implement these methods. |
| [IPrintPipelineManagerControl interface](nn-filterpipeline-iprintpipelinemanagercontrol.md) | The IPrintPipelineManagerControl interface is passed to each filter in the IPrintPipelineFilter |
| [IPrintPipelineProgressReport interface](nn-filterpipeline-iprintpipelineprogressreport.md) | A rendering filter uses the IPrintPipelineProgressReport interface to send progress status to a spooler. |
| [IPrintPipelinePropertyBag interface](nn-filterpipeline-iprintpipelinepropertybag.md) | The IPrintPipelinePropertyBag interface is implemented by the PrintFilterPipelineSvc service and is made available to filters through methods in the IPrintPipelineFilter interface. IprintPipelinePropertyBag inherits from the IUnknown interface. |
| [IPrintReadStream interface](nn-filterpipeline-iprintreadstream.md) | Filters use the IPrintReadStream interface to read data as a raw stream of bytes. |
| [IPrintReadStreamFactory interface](nn-filterpipeline-iprintreadstreamfactory.md) | The IPrintReadStreamFactory interface creates a stream reader that a filter can use to access the stream. For example, a filter could use this stream to access the per-user print ticket. |
| [IPrintWriteStream interface](nn-filterpipeline-iprintwritestream.md) | Filters use the IPrintWriteStream interface to write data as a raw stream of bytes. |
| [IPrintWriteStreamFlush interface](nn-filterpipeline-iprintwritestreamflush.md) | Filters use the IPrintWriteStreamFlush interface to explicitly flush data as a raw stream of bytes from a filter. This interface is retrieved through IPrintWriteStream |
| [IXpsDocument interface](nn-filterpipeline-ixpsdocument.md) | The IXpsDocument interface represents the root of an XPS document. |
| [IXpsDocumentConsumer interface](nn-filterpipeline-ixpsdocumentconsumer.md) | A filter uses the IXpsDocumentConsumer interface when it generates XPS content for the pipeline to consume. |
| [IXpsDocumentProvider interface](nn-filterpipeline-ixpsdocumentprovider.md) | The IxpsDocumentProvider interface provides interfaces to consume parts of a document. |
| [IXpsPartIterator interface](nn-filterpipeline-ixpspartiterator.md) | The IXpsPartIterator interface is an iterator for XPS parts. |

## Methods

| Title   | Description   |
| ---- |:----

# filterpipeline.h header



filterpipeline.h contains the following programming interfaces:



## Interfaces
| Title | Description |
| ---- |:---- |
| [IFixedDocument](nn-filterpipeline-ifixeddocument.md) | The IFixedDocument interface represents a fixed document for an XPS document sequence. |
| [IFixedDocumentSequence](nn-filterpipeline-ifixeddocumentsequence.md) | The IFixedDocumentSequence interface represents the fixed document sequence for an XPS document. |
| [IFixedPage](nn-filterpipeline-ifixedpage.md) | A filter uses the IFixedPage interface to work with fixed pages in an XPS document. |
| [IInterFilterCommunicator](nn-filterpipeline-iinterfiltercommunicator.md) | The IInterFilterCommunicator interface is implemented in an object that resides in the PrintFilterPipelineSvc service and is made available to filters through methods in the IPrintPipelineFilter interface. |
| [IPartBase](nn-filterpipeline-ipartbase.md) | The IPartBase interface is a common base for document part interfaces. |
| [IPartColorProfile](nn-filterpipeline-ipartcolorprofile.md) | The IPartColorProfile interface is the abstraction for an XPS color profile. |
| [IPartDiscardControl](nn-filterpipeline-ipartdiscardcontrol.md) | The filter pipeline supports the discard control. |
| [IPartFont](nn-filterpipeline-ipartfont.md) | The IPartFont interface is the abstraction for fonts in a part. |
| [IPartFont2](nn-filterpipeline-ipartfont2.md) | "." |
| [IPartImage](nn-filterpipeline-ipartimage.md) | The IPartImage interface is the abstraction for images in an XPS document. |
| [IPartPrintTicket](nn-filterpipeline-ipartprintticket.md) | The IPartPrintTicket interface is the abstraction for a print ticket in an XPS document. |
| [IPartResourceDictionary](nn-filterpipeline-ipartresourcedictionary.md) | The IPartResourceDictionary interface is the abstraction for an XPS resource dictionary. |
| [IPartThumbnail](nn-filterpipeline-ipartthumbnail.md) | The IPartThumbnail interface is an abstraction for thumbnails in an XPS document. |
| [IPrintClassObjectFactory](nn-filterpipeline-iprintclassobjectfactory.md) | TheIPrintClassObjectFactory interface creates print filter-related interfaces. |
| [IPrintPipelineFilter](nn-filterpipeline-iprintpipelinefilter.md) | The methods in the IPrintPipelineFilter interface are called for initialization and shutdown. A filter must implement these methods. |
| [IPrintPipelineManagerControl](nn-filterpipeline-iprintpipelinemanagercontrol.md) | The IPrintPipelineManagerControl interface is passed to each filter in the IPrintPipelineFilter::InitializeFilter method. |
| [IPrintPipelineProgressReport](nn-filterpipeline-iprintpipelineprogressreport.md) | A rendering filter uses the IPrintPipelineProgressReport interface to send progress status to a spooler. |
| [IPrintPipelinePropertyBag](nn-filterpipeline-iprintpipelinepropertybag.md) | The IPrintPipelinePropertyBag interface is implemented by the PrintFilterPipelineSvc service and is made available to filters through methods in the IPrintPipelineFilter interface. IprintPipelinePropertyBag inherits from the IUnknown interface. |
| [IPrintReadStream](nn-filterpipeline-iprintreadstream.md) | Filters use the IPrintReadStream interface to read data as a raw stream of bytes. |
| [IPrintReadStreamFactory](nn-filterpipeline-iprintreadstreamfactory.md) | The IPrintReadStreamFactory interface creates a stream reader that a filter can use to access the stream. For example, a filter could use this stream to access the per-user print ticket. |
| [IPrintWriteStream](nn-filterpipeline-iprintwritestream.md) | Filters use the IPrintWriteStream interface to write data as a raw stream of bytes. |
| [IPrintWriteStreamFlush](nn-filterpipeline-iprintwritestreamflush.md) | Filters use the IPrintWriteStreamFlush interface to explicitly flush data as a raw stream of bytes from a filter. This interface is retrieved through IPrintWriteStream::QueryInterface(). |
| [IXpsDocument](nn-filterpipeline-ixpsdocument.md) | The IXpsDocument interface represents the root of an XPS document. |
| [IXpsDocumentConsumer](nn-filterpipeline-ixpsdocumentconsumer.md) | A filter uses the IXpsDocumentConsumer interface when it generates XPS content for the pipeline to consume. |
| [IXpsDocumentProvider](nn-filterpipeline-ixpsdocumentprovider.md) | The IxpsDocumentProvider interface provides interfaces to consume parts of a document. |
| [IXpsPartIterator](nn-filterpipeline-ixpspartiterator.md) | The IXpsPartIterator interface is an iterator for XPS parts. |



## Functions
| Title | Description |
| ---- |:---- |
| [DrvPopulateFilterServices](nf-filterpipeline-drvpopulatefilterservices.md) | The DrvPopulateFilterServices function is called by the XPSDrv filter pipeline manager to allow the service provider to instantiate filter service objects in the filter pipeline property bag specified by the pPropertyBag parameter. |




## Enumerations
| Title | Description |
| ---- |:---- |
| [__MIDL___MIDL_itf_filterpipeline_0000_0000_0001](ne-filterpipeline-__midl___midl_itf_filterpipeline_0000_0000_0001.md) | The ExpsCompressionOptions enumeration describes compression options for an XPS part. |
| [__MIDL___MIDL_itf_filterpipeline_0000_0000_0002](ne-filterpipeline-__midl___midl_itf_filterpipeline_0000_0000_0002.md) | The EXpsFontOptions enumeration describes the font options for an XPS part. |
| [__MIDL___MIDL_itf_filterpipeline_0000_0000_0003](ne-filterpipeline-__midl___midl_itf_filterpipeline_0000_0000_0003.md) | The EXpsJobConsumption enumeration describes job consumption updates. |
| [__MIDL___MIDL_itf_filterpipeline_0000_0000_0004](ne-filterpipeline-__midl___midl_itf_filterpipeline_0000_0000_0004.md) | "." |