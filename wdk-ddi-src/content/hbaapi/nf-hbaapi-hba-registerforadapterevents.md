---
UID: NF.hbaapi.HBA_RegisterForAdapterEvents
title: HBA_RegisterForAdapterEvents
author: windows-driver-content
description: The HBA_RegisterForAdapterEvents routine registers the indicated user callback routine to call when an adapter event occurs.
old-location: storage\hba_registerforadapterevents.htm
old-project: storage
ms.assetid: b5e671dc-0583-4e5f-b537-3257b3f25479
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_RegisterForAdapterEvents
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
req.alt-api: HBA_RegisterForAdapterEvents
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

# HBA_RegisterForAdapterEvents function



## -description
<p>The <b>HBA_RegisterForAdapterEvents</b> routine registers the indicated user callback routine to call when an adapter event occurs. </p>


## -syntax

````
HBA_STATUS HBA_API HBA_RegisterForAdapterEvents(
   HBA_ADAPTER_CALLBACK callback,
   void                 *userData,
   HBA_HANDLE           handle,
   HBA_CALLBACKHANDLE   *callbackHandle
);
````


## -parameters
<dl>

### -param <i>callback</i> 

<dd>
<p>Pointer to a callback routine of type <a href="storage.hba_adapter_callback">HBA_ADAPTER_CALLBACK</a> that is called when an adapter is added to the system.</p>
</dd>

### -param <i>userData</i> 

<dd>
<p>Pointer to a buffer that is passed to the callback routine with each event. This data correlates the event with the source of the event registration. </p>
</dd>

### -param <i>handle</i> 

<dd>
<p>Contains a value returned by the routine <a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a> that identifies the HBA for which the adapter events are generated. </p>
</dd>

### -param <i>callbackHandle</i> 

<dd>
<p>Contains an opaque identifier that the user must pass to <a href="..\hbaapi\nf-hbaapi-hba-removecallback.md">HBA_RemoveCallback</a> to de-register the callback routine.</p>
</dd>
</dl>

## -returns
<p>The <b>HBA_RegisterForAdapterEvents</b> routine returns a value of type <a href="storage.hba_status">HBA_STATUS</a> that indicates the status of the HBA. In particular, this member should have one of the following values.</p><dl>
<dt><b>HBA_STATUS_OK</b></dt>
</dl><p>Returned if the callback routine was successfully registered. </p><dl>
<dt><b>HBA_STATUS_ERROR</b></dt>
</dl><p>Returned if an unspecified error occurred that prevented the registration of the callback routine. </p>

<p> </p>

## -remarks
<p>If the HBA referenced by <i>handle </i>is removed from the system, the callback function is called with event type of HBA_EVENT_ADAPTER_REMOVE.</p>

<p>If the configuration of the HBA referenced by <i>handle </i>is changed, the callback function is called with event type of HBA_EVENT_ADAPTER_CHANGE.</p>

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
<a href="storage.hba_adapter_callback">HBA_ADAPTER_CALLBACK</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_RegisterForAdapterEvents routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
