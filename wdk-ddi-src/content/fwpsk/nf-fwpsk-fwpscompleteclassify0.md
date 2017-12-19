---
UID: NF.fwpsk.FwpsCompleteClassify0
title: FwpsCompleteClassify0 function
author: windows-driver-content
description: A callout driver calls FwpsCompleteClassify0 to asynchronously complete a pended classify request.
old-location: netvista\fwpscompleteclassify0.htm
old-project: NetVista
ms.assetid: 995e86dc-fc26-4903-bc21-45475cb4e2bc
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FwpsCompleteClassify0
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
---

# FwpsCompleteClassify0 function



## -description
A callout driver calls 
  <b>FwpsCompleteClassify0</b> to asynchronously complete a pended classify request. The callout driver's 
  <a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a> function must have previously
  called 
  <a href="netvista.fwpspendclassify0">FwpsPendClassify0</a> to pend the classify
  request.



## -syntax

````
void NTAPI FwpsCompleteClassify0(
  _In_           UINT64             classifyHandle,
  _In_           UINT32             flags,
  _In_opt_ const FWPS_CLASSIFY_OUT0 *classifyOut
);
````


## -parameters

### -param classifyHandle [in]

The classification handle that identifies the callout driver's processing at the current layer.
     This handle is obtained by calling 
     <a href="netvista.fwpsacquireclassifyhandle0">
     FwpsAcquireClassifyHandle0</a>.


### -param flags [in]


      This parameter is reserved for future use. Set to zero.
     


### -param classifyOut [in, optional]

A pointer to a deep copy of the 
     <a href="netvista.fwps_classify_out0">FWPS_CLASSIFY_OUT0</a> structure that was originally
     passed to the 
     <a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a> call when the classification was pended. When classifying asynchronously, the members
     of this structure can be set the same way as they would be in the callout driver's 
     <i>classifyFn</i> function when classifying inline.
     

If this parameter is used, the classification is taken as the callout driver's final decision. If set
     to <b>NULL</b>, the indication will be reauthorized.


## -returns
None.


## -remarks
<b>FwpsCompleteClassify0</b> must be called after a callout driver has called 
    <a href="netvista.fwpspendclassify0">FwpsPendClassify0</a> to remove the
    classification from its pended state.

After calling this function, 
    <a href="netvista.fwpsreleaseclassifyhandle0">FwpsReleaseClassifyHandle0</a> must
    be called to free the system resources associated with the classification handle.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 7.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a>
</dt>
<dt>
<a href="netvista.fwps_classify_out0">FWPS_CLASSIFY_OUT0</a>
</dt>
<dt>
<a href="netvista.fwpsacquireclassifyhandle0">FwpsAcquireClassifyHandle0</a>
</dt>
<dt>
<a href="netvista.fwpspendclassify0">FwpsPendClassify0</a>
</dt>
<dt>
<a href="netvista.fwpsreleaseclassifyhandle0">FwpsReleaseClassifyHandle0</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20FwpsCompleteClassify0 function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

