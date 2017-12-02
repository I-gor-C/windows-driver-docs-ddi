---
UID: NC.portcls.PCPFNEVENT_HANDLER
title: PCPFNEVENT_HANDLER
author: windows-driver-content
description: An EventHandler routine processes event requests.
old-location: audio\eventhandler.htm
old-project: audio
ms.assetid: 06239870-8ed8-49c9-a9d4-fd3e28f3ab58
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BarcodeSymbologyAttributesData, BarcodeSymbologyAttributesData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EventHandler
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# PCPFNEVENT_HANDLER callback



## -description
<p>An <code>EventHandler</code> routine processes event requests.</p>


## -prototype

````
PCPFNEVENT_HANDLER EventHandler;

NTSTATUS EventHandler(
  _In_ PPCEVENT_REQUEST EventRequest
)
{ ... }
````


## -parameters
<dl>

### -param EventRequest [in]

<dd>
<p>Pointer to an initialized <a href="..\portcls\ns-portcls--pcevent-request.md">PCEVENT_REQUEST</a> structure</p>
</dd>
</dl>

## -returns
<p>The event handler returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>Each event that a miniport driver exposes is associated with an event handler. The purpose of the event handler is to process event requests from the port driver and its clients. <i>EventRequest</i> is an input parameter to the handler that contains the following information about the event:</p>

<p>The event set GUID and event ID.</p>

<p>How the event is to be triggered.</p>

<p>Pointers to the target miniport object and (for a pin) stream object.</p>

<p>This is similar to the type of information that is provided with property requests.</p>

<p>The miniport driver exposes its event handlers through its <a href="audio.iminiport_getdescription">IMiniport::GetDescription</a> method. This method outputs a descriptor structure (see <a href="audio.pcfilter_descriptor">PCFILTER_DESCRIPTOR</a>) that defines the filter that the miniport driver and its associated port driver implement together. This structure contains a pointer to the miniport driver's automation table (see <a href="audio.pcautomation_table">PCAUTOMATION_TABLE</a>), which in turn contains a pointer to an array of the miniport driver's events. Each array element is a <a href="audio.pcevent_item">PCEVENT_ITEM</a> structure and contains a PCPFNEVENT_HANDLER function pointer to the handler for the event.</p>

<p>The <code>EventHandler</code> routine must reside in nonpaged memory.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="audio.iportevents_addeventtoeventlist">IPortEvents::AddEventToEventList</a>
</dt>
<dt>
<a href="audio.iportevents_generateeventlist">IPortEvents::GenerateEventList</a>
</dt>
<dt>
<a href="..\portcls\ns-portcls--pcevent-request.md">PCEVENT_REQUEST</a>
</dt>
<dt>
<a href="audio.iminiport_getdescription">IMiniport::GetDescription</a>
</dt>
<dt>
<a href="audio.pcfilter_descriptor">PCFILTER_DESCRIPTOR</a>
</dt>
<dt>
<a href="audio.pcautomation_table">PCAUTOMATION_TABLE</a>
</dt>
<dt>
<a href="audio.pcevent_item">PCEVENT_ITEM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PCPFNEVENT_HANDLER callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
