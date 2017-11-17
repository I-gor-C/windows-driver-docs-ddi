---
UID: NF.fwpsk.FwpsCompleteClassify0
title: FwpsCompleteClassify0
author: windows-driver-content
description: A callout driver calls FwpsCompleteClassify0 to asynchronously complete a pended classify request.
old-location: netvista\fwpscompleteclassify0.htm
ms.assetid: 995e86dc-fc26-4903-bc21-45475cb4e2bc
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsCompleteClassify0
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
ms.keywords: FwpsCompleteClassify0
req.iface: 
---

# FwpsCompleteClassify0 function



## -description
<p>A callout driver calls 
  <b>FwpsCompleteClassify0</b> to asynchronously complete a pended classify request. The callout driver's 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> function must have previously
  called 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff551197">FwpsPendClassify0</a> to pend the classify
  request.</p>


## -syntax

````
void NTAPI FwpsCompleteClassify0(
  _In_           UINT64             classifyHandle,
  _In_           UINT32             flags,
  _In_opt_ const FWPS_CLASSIFY_OUT0 *classifyOut
);
````


## -parameters
<dl>

### -param <i>classifyHandle</i> [in]

<dd>
<p>The classification handle that identifies the callout driver's processing at the current layer.
     This handle is obtained by calling 
     <a href="https://msdn.microsoft.com/7348d937-6541-47a7-ae70-7d851d41bc1a">
     FwpsAcquireClassifyHandle0</a>.</p>
</dd>

### -param <i>flags</i> [in]

<dd>
<p>
      This parameter is reserved for future use. Set to zero.
     </p>
</dd>

### -param <i>classifyOut</i> [in, optional]

<dd>
<p>A pointer to a deep copy of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure that was originally
     passed to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> call when the classification was pended. When classifying asynchronously, the members
     of this structure can be set the same way as they would be in the callout driver's 
     <i>classifyFn</i> function when classifying inline.
     </p>
<p>If this parameter is used, the classification is taken as the callout driver's final decision. If set
     to <b>NULL</b>, the indication will be reauthorized.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p><b>FwpsCompleteClassify0</b> must be called after a callout driver has called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551197">FwpsPendClassify0</a> to remove the
    classification from its pended state.</p>

<p>After calling this function, 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551208">FwpsReleaseClassifyHandle0</a> must
    be called to free the system resources associated with the classification handle.</p>

<p><b>FwpsCompleteClassify0</b> must be called after a callout driver has called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551197">FwpsPendClassify0</a> to remove the
    classification from its pended state.</p>

<p>After calling this function, 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551208">FwpsReleaseClassifyHandle0</a> must
    be called to free the system resources associated with the classification handle.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550085">FwpsAcquireClassifyHandle0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551197">FwpsPendClassify0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551208">FwpsReleaseClassifyHandle0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsCompleteClassify0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
