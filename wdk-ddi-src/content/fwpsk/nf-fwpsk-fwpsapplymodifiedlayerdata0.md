---
UID: NF.fwpsk.FwpsApplyModifiedLayerData0
title: FwpsApplyModifiedLayerData0
author: windows-driver-content
description: The FwpsApplyModifiedLayerData0 function applies changes to layer-specific data made after a call to FwpsAcquireWritableLayerDataPointer0.Note  FwpsApplyModifiedLayerData0 is a specific version of FwpsApplyModifiedLayerData.
old-location: netvista\fwpsapplymodifiedlayerdata0.htm
old-project: netvista
ms.assetid: d32c19b6-462e-48e3-b22b-02542dca9cc4
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpsApplyModifiedLayerData0
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
req.alt-api: FwpsApplyModifiedLayerData0
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

# FwpsApplyModifiedLayerData0 function



## -description
<p>The 
  <b>FwpsApplyModifiedLayerData0</b> function applies changes to layer-specific data made after a call to 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff550087">FwpsAcquireWritableLayerDataPointer0</a>.</p>


## -syntax

````
void NTAPI FwpsApplyModifiedLayerData0(
  _In_ UINT64 classifyHandle,
  _In_ PVOID  modifiedLayerData,
  _In_ UINT32 flags
);
````


## -parameters
<dl>

### -param <i>classifyHandle</i> [in]

<dd>
<p>The classification handle that identifies the callout driver's processing at the current layer.
     This handle is obtained by calling 
     <a href="..\fwpsk\nf-fwpsk-fwpsacquireclassifyhandle0.md">
     FwpsAcquireClassifyHandle0</a>.</p>
</dd>

### -param <i>modifiedLayerData</i> [in]

<dd>
<p>The data buffer obtained by calling 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff550087">FwpsAcquireWritableLayerDataPointer0</a> with members modified by the callout driver. Supported data
     types are defined as structures.</p>
</dd>

### -param <i>flags</i> [in]

<dd>
<p>
      The options to use with this function call. This flag can have the following
      value.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="FWPS_CLASSIFY_FLAG_REAUTHORIZE_IF_MODIFIED_BY_OTHERS"></a><a id="fwps_classify_flag_reauthorize_if_modified_by_others"></a><dl>

### -param <b>FWPS_CLASSIFY_FLAG_REAUTHORIZE_IF_MODIFIED_BY_OTHERS</b>

</dl>
</td>
<td width="60%">
<p>When set, this flag specifies that data at the layer of the pended classify action should be reauthorized if another callout driver modifies the data before the classification is completed. Use this flag only with pended classify and not inline classify, as its use with inline classify can lead to indeterminate results. If you do call this API for inline classify, set flags to zero.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p><b>FwpsApplyModifiedLayerData0</b> should be called once for every call made to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff550087">FwpsAcquireWritableLayerDataPointer0</a>, even if the callout driver didn't modify any data.</p>

<p><b>FwpsApplyModifiedLayerData0</b> should be called once for every call made to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff550087">FwpsAcquireWritableLayerDataPointer0</a>, even if the callout driver didn't modify any data.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551231">FWPS_CONNECT_REQUEST0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552389">FWPS_FILTER1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550085">FwpsAcquireClassifyHandle0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsacquirewritablelayerdatapointer0.md">
   FwpsAcquireWritableLayerDataPointer0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551208">FwpsReleaseClassifyHandle0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsApplyModifiedLayerData0 function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
