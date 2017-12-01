---
UID: NF.fwpmk.FwpmBfeStateGet0
title: FwpmBfeStateGet0
author: windows-driver-content
description: The FwpmBfeStateGet0 function retrieves the current state of the filter engine.Note  FwpmBfeStateGet0 is a specific version of FwpmBfeStateGet.
old-location: netvista\fwpmbfestateget0.htm
old-project: netvista
ms.assetid: f165c5a0-6f8e-495f-90b9-62d0d8982456
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FwpmBfeStateGet0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpmk.h
req.include-header: Fwpmk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpmBfeStateGet0
req.alt-loc: Fwpkclnt.lib,Fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# FwpmBfeStateGet0 function



## -description
<p>The 
  <b>FwpmBfeStateGet0</b> function retrieves the current state of the filter engine.</p>


## -syntax

````
FWPM_SERVICE_STATE NTAPI FwpmBfeStateGet0(void);
````


## -parameters


## -returns
<p>The 
     <b>FwpmBfeStateGet0</b> function returns one of the following values.</p><dl>
<dt><b>FWPM_SERVICE_STOPPED</b></dt>
</dl><p>The filter engine is not running.</p><dl>
<dt><b>FWPM_SERVICE_START_PENDING</b></dt>
</dl><p>The filter engine is starting.</p><dl>
<dt><b>FWPM_SERVICE_STOP_PENDING</b></dt>
</dl><p>The filter engine is stopping.</p><dl>
<dt><b>FWPM_SERVICE_RUNNING</b></dt>
</dl><p>The filter engine is running.</p>

<p> </p>

<p>The 
     <b>FwpmBfeStateGet0</b> function returns one of the following values.</p><dl>
<dt><b>FWPM_SERVICE_STOPPED</b></dt>
</dl><p>The filter engine is not running.</p><dl>
<dt><b>FWPM_SERVICE_START_PENDING</b></dt>
</dl><p>The filter engine is starting.</p><dl>
<dt><b>FWPM_SERVICE_STOP_PENDING</b></dt>
</dl><p>The filter engine is stopping.</p><dl>
<dt><b>FWPM_SERVICE_RUNNING</b></dt>
</dl><p>The filter engine is running.</p>

<p> </p>

<p>The 
     <b>FwpmBfeStateGet0</b> function returns one of the following values.</p><dl>
<dt><b>FWPM_SERVICE_STOPPED</b></dt>
</dl><p>The filter engine is not running.</p><dl>
<dt><b>FWPM_SERVICE_START_PENDING</b></dt>
</dl><p>The filter engine is starting.</p><dl>
<dt><b>FWPM_SERVICE_STOP_PENDING</b></dt>
</dl><p>The filter engine is stopping.</p><dl>
<dt><b>FWPM_SERVICE_RUNNING</b></dt>
</dl><p>The filter engine is running.</p>

<p> </p>

## -remarks
<p>A callout driver calls the 
    <b>FwpmBfeStateGet0</b> function to retrieve the current state of the filter engine. For a callout driver
    to open a session to the filter engine, the filter engine must  be currently running.</p>

<p>Before calling <b>FwpmBfeStateGet0</b>, the callout driver  must call the 
    <a href="..\fwpmk\nf-fwpmk-fwpmbfestatesubscribechanges0.md">FwpmBfeStateSubscribeChanges0</a> function to register a callback function that is called whenever the
    state of the filter engine changes.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpmk.h (include Fwpmk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fwpmk\nf-fwpmk-fwpmbfestatesubscribechanges0.md">
   FwpmBfeStateSubscribeChanges0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpmBfeStateGet0 function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
