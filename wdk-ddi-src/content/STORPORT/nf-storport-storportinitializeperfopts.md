---
UID: NF.storport.StorPortInitializePerfOpts
title: StorPortInitializePerfOpts
author: windows-driver-content
description: The StorPortInitializePerfOpts function initializes the performance optimizations that both the miniport driver and the Storport driver support using a PERF_CONFIGURATION_DATA structure.
old-location: storage\storportinitializeperfopts.htm
ms.assetid: fbaf864c-d499-456c-be3b-b486c637877e
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortInitializePerfOpts
req.alt-loc: Storport.h
req.ddi-compliance: StorPortPerfOpts
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: StorPortInitializePerfOpts
req.iface: 
req.product: Windows 10 or later.
---

# StorPortInitializePerfOpts function



## -description
<p>The <b>StorPortInitializePerfOpts</b> function initializes the performance optimizations that both the miniport driver and the Storport driver support using a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563845">PERF_CONFIGURATION_DATA</a> structure.</p>


## -syntax

````
ULONG StorPortInitializePerfOpts(
  _In_    PVOID                    HwDeviceExtension,
  _In_    BOOLEAN                  Query,
  _Inout_ PPERF_CONFIGURATION_DATA PerfConfigData
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA). This parameter must not be <b>NULL</b>.</p>
</dd>

### -param <i>Query</i> [in]

<dd>
<p>If set to <b>TRUE</b>, Storport will set the flags in <i>PerfConfigData</i> corresponding to the optimizations Storport supports. If set to <b>FALSE</b>, Storport will initialize the optimizations specified by the flags in <i>PerfConfigData</i>.</p>
</dd>

### -param <i>PerfConfigData</i> [in, out]

<dd>
<p>A pointer to a PERF_CONFIGURATION_DATA structure that is supplied by the miniport driver. This parameter must not be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>StorPortInitializePerfOpts returns one of the following status values:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the performance optimization settings have been applied.</p>

<p>Or if <i>Query</i> is set to <b>TRUE</b>,  the <b>Flags</b> member of the structure pointed to by <i>PerfConfigData</i> contains the supported flags.</p><dl>
<dt><b>STOR_STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The miniport driver set a flag in <i>PerfConfigData</i> that Storport did not recognize, or the miniport driver has called this routine from outside the miniport-driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff557396">HwStorInitialize</a> routine.</p><dl>
<dt><b>STOR_STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Unable to allocate internal structures to support the requested optimizations.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Either the <i>HwDeviceExtension</i> parameter or the <i>PerfConfigData</i> parameter was <b>NULL</b>.</p>

<p> </p>

## -remarks
<p>
    The miniport driver can call <b>StorPortInitializePerfOpts</b> only during the miniport-supplied   <a href="https://msdn.microsoft.com/library/windows/hardware/ff557396">HwStorInitialize</a> routine or <a href="https://msdn.microsoft.com/library/windows/hardware/ff557407">HwStorPassiveInitializeRoutine</a> routine.
   </p>

<p>Available performance optimizations depend on the version of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563845">PERF_CONFIGURATION_DATA</a>. Setting the <b>Version</b> member to <b>STOR_PERF_VERSION</b> will allow all supported optimizations to be selected.</p>

<p>
    The miniport driver can call <b>StorPortInitializePerfOpts</b> only during the miniport-supplied   <a href="https://msdn.microsoft.com/library/windows/hardware/ff557396">HwStorInitialize</a> routine or <a href="https://msdn.microsoft.com/library/windows/hardware/ff557407">HwStorPassiveInitializeRoutine</a> routine.
   </p>

<p>Available performance optimizations depend on the version of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563845">PERF_CONFIGURATION_DATA</a>. Setting the <b>Version</b> member to <b>STOR_PERF_VERSION</b> will allow all supported optimizations to be selected.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454270">StorPortPerfOpts</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563845">PERF_CONFIGURATION_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20StorPortInitializePerfOpts function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
