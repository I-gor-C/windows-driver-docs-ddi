---
UID: NF.hbaapi.HBA_RegisterForLinkEvents
title: HBA_RegisterForLinkEvents
author: windows-driver-content
description: The HBA_RegisterForLinkEvents routine registers with a specified adapter for asynchronous fabric link-level events.
old-location: storage\hba_registerforlinkevents.htm
old-project: storage
ms.assetid: f0e6834c-b827-4342-83f1-5980f8edce24
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_RegisterForLinkEvents
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_RegisterForLinkEvents
req.alt-loc: Hbaapi.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hbaapi.lib
req.dll: Hbaapi.dll
req.irql: 
req.iface: 
---

# HBA_RegisterForLinkEvents function



## -description
<p>The <b>HBA_RegisterForLinkEvents</b> routine registers with a specified adapter for asynchronous fabric link-level events. </p>


## -syntax

````
HBA_STATUS HBA_API HBA_RegisterForLinkEvents(
   HBA_LINK_CALLBACK  callback,
   void               *userData,
   void               *pRLIRBuffer,
   HBA_UINT32         RLIRBufferSize,
   HBA_HANDLE         handle,
   HBA_CALLBACKHANDLE *callbackHandle
);
````


## -parameters
<dl>

### -param callback 

<dd>
<p>Pointer to a callback routine of type <a href="storage.hba_link_callback">HBA_LINK_CALLBACK</a> to call when the event occurs. </p>
</dd>

### -param userData 

<dd>
<p>Pointer to user input data that is passed to the callback routine when it is called with each occurrence of the event. This data can synchronize the event handling with event registration.</p>
</dd>

### -param pRLIRBuffer 

<dd>
<p>Pointer to registered link incident report (RLIR) data that is passed to the callback routine with each occurrence of the event. This data is overwritten by the callback routine each time it is called. </p>
</dd>

### -param RLIRBufferSize 

<dd>
<p>Contains the size, in bytes, of the buffer at <i>pRLIRBuffer</i>.</p>
</dd>

### -param handle 

<dd>
<p>Contains a value returned by the routine <a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a> that identifies the HBA for which event callbacks are requested.</p>
</dd>

### -param callbackHandle 

<dd>
<p>Pointer to an opaque identifier that may be used to deregister the caller and suspend calls to the callback routine when events occur.</p>
</dd>
</dl>

## -returns
<p>The <b>HBA_RegisterForLinkEvents</b> routine returns a value of type <a href="storage.hba_status">HBA_STATUS</a> that indicates the status of the HBA. In particular, <b>HBA_RegisterForLinkEvents</b> returns one of the following values.</p><dl>
<dt><b>HBA_STATUS_OK</b></dt>
</dl><p>Returned if the callback registration was successful. </p><dl>
<dt><b>HBA_STATUS_ERROR_NOT_SUPPORTED</b></dt>
</dl><p>Returned if either the library or the system does not support events. </p><dl>
<dt><b>HBA_STATUS_ERROR</b></dt>
</dl><p>Returned if an unspecified error occurred that prevented the registration of the callback routine. </p>

<p> </p>

## -remarks
<p>Only RLIR events are reported. To stop event delivery, call <a href="..\hbaapi\nf-hbaapi-hba-removecallback.md">HBA_RemoveCallback</a>.</p>

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
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.hba_link_callback">HBA_LINK_CALLBACK</a>
</dt>
<dt>
<a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a>
</dt>
<dt>
<a href="..\hbaapi\nf-hbaapi-hba-removecallback.md">HBA_RemoveCallback</a>
</dt>
<dt>
<a href="storage.hba_status">HBA_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_RegisterForLinkEvents routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
