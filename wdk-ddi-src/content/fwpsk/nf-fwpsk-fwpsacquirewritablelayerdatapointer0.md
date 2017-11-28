---
UID: NF.fwpsk.FwpsAcquireWritableLayerDataPointer0
title: FwpsAcquireWritableLayerDataPointer0
author: windows-driver-content
description: The FwpsAcquireWritableLayerDataPointer0 function returns layer-specific data that can be inspected and changed.Note  FwpsAcquireWritableLayerDataPointer0 is a specific version of FwpsAcquireWritableLayerDataPointer.
old-location: netvista\fwpsacquirewritablelayerdatapointer0.htm
old-project: netvista
ms.assetid: 79816d01-bf27-49d0-b6f1-083b7e87cc4e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpsAcquireWritableLayerDataPointer0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsAcquireWritableLayerDataPointer0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
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

# FwpsAcquireWritableLayerDataPointer0 function



## -description
<p>The 
  <b>FwpsAcquireWritableLayerDataPointer0</b> function returns layer-specific data that can be inspected and
  changed.</p>


## -syntax

````
NTSTATUS NTAPI FwpsAcquireWritableLayerDataPointer0(
  _In_    UINT64             classifyHandle,
  _In_    UINT64             filterId,
  _In_    UINT32             flags,
  _Out_   PVOID              *writableLayerData,
  _Inout_ FWPS_CLASSIFY_OUT0 *classifyOut
);
````


## -parameters
<dl>

### -param <i>classifyHandle</i> [in]

<dd>
<p>A handle for the classify request.
     This handle is obtained by calling 
     <a href="..\fwpsk\nf-fwpsk-fwpsacquireclassifyhandle0.md">
     FwpsAcquireClassifyHandle0</a>.</p>
</dd>

### -param <i>filterId</i> [in]

<dd>
<p>The value of the 
     <b>FilterId</b> member of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> function's 
     <i>filter</i> parameter. For more information about the 
     <b>FilterId</b> member, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552389">FWPS_FILTER1</a>.</p>
</dd>

### -param <i>flags</i> [in]

<dd>
<p>Reserved for future use. Set to zero.</p>
</dd>

### -param <i>writableLayerData</i> [out]

<dd>
<p>A data buffer that contains the modifiable data for the layer. The supported data types, which are listed in the following Remarks section, are defined as
     structures. On return, the data can be accessed by casting the void pointer to the appropriate structure
     type.</p>
</dd>

### -param <i>classifyOut</i> [in, out]

<dd>
<p>Set to the 
     <i>classifyOut</i> parameter of the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> function. The 
     <i>classifyOut</i> parameter of 
     classifyFn is listed as an output parameter in the header, but it contains enough information on
     input to be useful to the engine when passed to 
     <b>FwpsAcquireWritableLayerDataPointer0</b>.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsAcquireWritableLayerDataPointer0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The callback function was successfully registered.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p><b>FwpsAcquireWritableLayerDataPointer0</b> sets the following members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure:<ul>
<li><i>classifyOut</i>-&gt;<b>actionType</b> = <b>FWP_ACTION_BLOCK</b></li>
<li><i>classifyOut</i>-&gt;<b>rights</b> = ~<b>FWPS_RIGHT_ACTION_WRITE</b></li>
</ul>
</p>

<p>For every call to this function, you must make a matching call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551137">FwpsApplyModifiedLayerData0</a> to
    finalize the changes that were made, even if your callout driver didn't modify any data. If you do not make the call to <b>FwpsApplyModifiedLayerData0</b>, this could result in the classify not completing correctly.</p>

<p>The following structures are defined to contain modifiable layer data. The pointer set on output as
    the 
    <i>writableLayerData</i> parameter can be cast to one of these types:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551221">FWPS_BIND_REQUEST0</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551231">FWPS_CONNECT_REQUEST0</a>
</p>

<p><b>FwpsAcquireWritableLayerDataPointer0</b> sets the following members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure:<ul>
<li><i>classifyOut</i>-&gt;<b>actionType</b> = <b>FWP_ACTION_BLOCK</b></li>
<li><i>classifyOut</i>-&gt;<b>rights</b> = ~<b>FWPS_RIGHT_ACTION_WRITE</b></li>
</ul>
</p>

<p>For every call to this function, you must make a matching call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551137">FwpsApplyModifiedLayerData0</a> to
    finalize the changes that were made, even if your callout driver didn't modify any data. If you do not make the call to <b>FwpsApplyModifiedLayerData0</b>, this could result in the classify not completing correctly.</p>

<p>The following structures are defined to contain modifiable layer data. The pointer set on output as
    the 
    <i>writableLayerData</i> parameter can be cast to one of these types:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551221">FWPS_BIND_REQUEST0</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551231">FWPS_CONNECT_REQUEST0</a>
</p>

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
<p>Available starting with Windows 7.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551221">FWPS_BIND_REQUEST0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551231">FWPS_CONNECT_REQUEST0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552389">FWPS_FILTER1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550085">FwpsAcquireClassifyHandle0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551137">FwpsApplyModifiedLayerData0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551208">FwpsReleaseClassifyHandle0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsAcquireWritableLayerDataPointer0 function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
