---
UID: NF.wdm.KeConvertAuxiliaryCounterToPerformanceCounter
title: KeConvertAuxiliaryCounterToPerformanceCounter
author: windows-driver-content
description: The KeConvertAuxiliaryCounterToPerformanceCounter routine converts the specified auxiliary counter value into a performance counter value.
old-location: kernel\keconvertauxiliarycountertoperformancecounter.htm
old-project: kernel
ms.assetid: 90F4CE6D-F51A-4B18-B328-63AF4D71A690
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeConvertAuxiliaryCounterToPerformanceCounter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeConvertAuxiliaryCounterToPerformanceCounter
req.alt-loc: Hal.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: Hal.dll
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# KeConvertAuxiliaryCounterToPerformanceCounter function



## -description
<p>The  <b>KeConvertAuxiliaryCounterToPerformanceCounter</b> routine converts the specified auxiliary counter value into a performance  counter value.


</p>


## -syntax

````
NTSTATUS KeConvertAuxiliaryCounterToPerformanceCounter(
  _In_      ULONG64  AuxiliaryCounterValue,
  _Out_     PULONG64 PerformanceCounterValue,
  _Out_opt_ PULONG64 ConversionError
);
````


## -parameters
<dl>

### -param <i>AuxiliaryCounterValue</i> [in]

<dd>
<p>The auxiliary counter value to convert.</p>
</dd>

### -param <i>PerformanceCounterValue</i> [out]

<dd>
<p>A pointer to the variable that contains the converted performance counter value.</p>
</dd>

### -param <i>ConversionError</i> [out, optional]

<dd>
<p>A pointer to a variable that contains the estimated conversion error in units of nanosecond.</p>
</dd>
</dl>

## -returns
<p><b>KeConvertAuxiliaryCounterToPerformanceCounter</b> can return one of the following:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The conversion succeeded.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>Auxiliary counter is not supported.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER </b></dt>
</dl><p>The <i>AuxiliaryCounterValue</i> value is not valid. For example, the value is earlier than the last system boot/recovery, or is out of the +/- 10s range compared to the current auxiliary counter value.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL </b></dt>
</dl><p>The routine cannot convert the specified value with acceptable accuracy.</p>

<p> </p>

## -remarks
<p>Make sure that the specified auxiliary counter value is within +/- 10s compared to the current value.

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
<p>Available starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hal.dll</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-keconvertperformancecountertoauxiliarycounter.md">KeConvertPerformanceCounterToAuxiliaryCounter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeConvertAuxiliaryCounterToPerformanceCounter routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
