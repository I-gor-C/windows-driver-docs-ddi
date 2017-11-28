---
UID: NF.wdm.PoFxQueryCurrentComponentPerfState
title: PoFxQueryCurrentComponentPerfState
author: windows-driver-content
description: The PoFxQueryCurrentComponentPerfState routine retrieves the active performance state in a component's performance state set.
old-location: kernel\pofxquerycurrentcomponentperfstate.htm
old-project: kernel
ms.assetid: DFB59020-1F4A-4ABB-8BBE-85F9C8615249
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PoFxQueryCurrentComponentPerfState
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
req.alt-api: PoFxQueryCurrentComponentPerfState
req.alt-loc: Ntoskrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: Ntoskrnl.exe
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PoFxQueryCurrentComponentPerfState function



## -description
<p>The <b>PoFxQueryCurrentComponentPerfState</b> routine retrieves the active performance state in a component's performance state set. </p>


## -syntax

````
NTSTATUS PoFxQueryCurrentComponentPerfState(
  _In_ POHANDLE   Handle,
  _In_ ULONG      Flags,
  _In_ ULONG      Component,
  _In_ ULONG      SetIndex,
  _In_ PULONGLONG CurrentPerf
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>A handle that represents the registration of the device with power management framework (PoFx). The device driver previously received this handle from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439521">PoFxRegisterDevice</a> routine.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Set to 0. Currently, no flags are defined for this routine.</p>
</dd>

### -param <i>Component</i> [in]

<dd>
<p>The index that identifies the component whose performance state is being retrieved. This parameter is an index into the <b>Components</b> array in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439585">PO_FX_DEVICE</a> structure that the device driver used to register the device with PoFx. If the <b>Components</b> array contains N elements, component indexes range from 0 to N–1.</p>
</dd>

### -param <i>SetIndex</i> [in]

<dd>
<p>The index that identifies the performance state set whose performance is being queried. This parameter is an index into the <b>PerfStateSets</b> array in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn939832">PO_FX_COMPONENT_PERF_INFO</a> structure that the device driver used to register the component performance states with PoFx. If the <b>PerfStateSets</b> array contains N elements, performance state set indexes range from 0 to N–1.</p>
</dd>

### -param <i>CurrentPerf</i> [in]

<dd>
<p>A pointer to variable in which the current performance state for the specified performance state set is returned. For more information about the value that is returned, see Remarks. </p>
</dd>
</dl>

## -returns
<p><b>PoFxQueryCurrentComponentPerfState</b> returns <b>STATUS_SUCCESS</b> if the requested operation succeeds. Possible error return values include the following status codes.</p><dl>
<dt><b><b>STATUS_INVALID_PARAMETER</b></b></dt>
</dl><p>The caller supplied an invalid index for the component or component state set.</p>

<p> </p>

## -remarks
<p>A driver can call the <b>PoFxQueryCurrentComponentPerfState</b> routine to retrieve the current performance state of a given performance state set for a component. If the call succeeds, the <i>CurrentPerf</i> parameter is overwritten with a pointer to a value that specifies the current performance state of the set. This value may be one of the following, depending on the contents of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn939833">PO_FX_COMPONENT_PERF_SET</a> structure that the driver passed to the <a href="https://msdn.microsoft.com/library/windows/hardware/dn939778">PoFxRegisterComponentPerfStates</a> routine:</p>

<p>This call always executes synchronously.</p>

<p>A driver can call the <b>PoFxQueryCurrentComponentPerfState</b> routine to retrieve the current performance state of a given performance state set for a component. If the call succeeds, the <i>CurrentPerf</i> parameter is overwritten with a pointer to a value that specifies the current performance state of the set. This value may be one of the following, depending on the contents of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn939833">PO_FX_COMPONENT_PERF_SET</a> structure that the driver passed to the <a href="https://msdn.microsoft.com/library/windows/hardware/dn939778">PoFxRegisterComponentPerfStates</a> routine:</p>

<p>This call always executes synchronously.</p>

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
<dt>Ntoskrnl.exe</dt>
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
<a href="https://msdn.microsoft.com/D5341D6D-7C71-43CB-9C70-7E939B32C33F">Device Performance State Management</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn939778">PoFxRegisterComponentPerfStates</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn939833">PO_FX_COMPONENT_PERF_SET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn939832">PO_FX_COMPONENT_PERF_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxQueryCurrentComponentPerfState routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
