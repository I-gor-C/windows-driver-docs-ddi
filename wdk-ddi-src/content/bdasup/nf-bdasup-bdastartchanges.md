---
UID: NF.bdasup.BdaStartChanges
title: BdaStartChanges
author: windows-driver-content
description: The BdaStartChanges function initiates the setting of new BDA topology changes.
old-location: stream\bdastartchanges.htm
old-project: stream
ms.assetid: ee54b382-7b69-4d8d-8728-fe2bff7884cf
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: BdaStartChanges
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: bdasup.h
req.include-header: Bdasup.h
req.target-type: Desktop
req.target-min-winverclnt: Available on Microsoft Windows XP and later operating systems. This routine is available on the Windows 2000 platform only if Microsoft DirectX 9.0 and later is installed on that platform.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BdaStartChanges
req.alt-loc: Bdasup.lib,Bdasup.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Bdasup.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# BdaStartChanges function



## -description
<p>The <b>BdaStartChanges</b> function initiates the setting of new BDA topology changes. </p>


## -syntax

````
NTSTATUS BdaStartChanges(
  _In_ PIRP Irp
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Points to the IRP for the request to initiate changes. The BDA minidriver receives this IRP with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563418">KSMETHOD_BDA_START_CHANGES</a> request.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS or an appropriate error code. </p>

## -remarks
<p>A BDA minidriver calls the <b>BdaStartChanges</b> function to initiate the setting of new BDA topology changes after the minidriver receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563418">KSMETHOD_BDA_START_CHANGES</a> request of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563403">KSMETHODSETID_BdaChangeSync</a> method set from the network provider. BDA minidrivers define dispatch and filter-automation tables so that those minidrivers either dispatch the <b>BdaStartChanges</b> function directly or intercept this request using an internal method (<a href="https://msdn.microsoft.com/library/windows/hardware/ff567191">KStrMethodHandler</a>), which then calls the <b>BdaStartChanges</b> function. For example, BDA minidrivers that intercept this request can obtain a pointer to the BDA filter from the passed IRP so that they can subsequently reset pending filter resources to the new requirements and set the change state of the filter to BDA_CHANGES_COMPLETE. See <a href="NULL">Defining Automation Tables</a> and <a href="NULL">Changing BDA Filter Properties</a> for more information. </p>

<p>Calling the <b>BdaStartChanges</b> function causes any previously requested topology changes that have not yet been committed to be ignored.</p>

<p>A BDA minidriver calls the <b>BdaStartChanges</b> function to initiate the setting of new BDA topology changes after the minidriver receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563418">KSMETHOD_BDA_START_CHANGES</a> request of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563403">KSMETHODSETID_BdaChangeSync</a> method set from the network provider. BDA minidrivers define dispatch and filter-automation tables so that those minidrivers either dispatch the <b>BdaStartChanges</b> function directly or intercept this request using an internal method (<a href="https://msdn.microsoft.com/library/windows/hardware/ff567191">KStrMethodHandler</a>), which then calls the <b>BdaStartChanges</b> function. For example, BDA minidrivers that intercept this request can obtain a pointer to the BDA filter from the passed IRP so that they can subsequently reset pending filter resources to the new requirements and set the change state of the filter to BDA_CHANGES_COMPLETE. See <a href="NULL">Defining Automation Tables</a> and <a href="NULL">Changing BDA Filter Properties</a> for more information. </p>

<p>Calling the <b>BdaStartChanges</b> function causes any previously requested topology changes that have not yet been committed to be ignored.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available on Microsoft Windows XP and later operating systems. This routine is available on the Windows 2000 platform only if Microsoft DirectX 9.0 and later is installed on that platform.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bdasup.h (include Bdasup.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Bdasup.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556518">BDA_CHANGE_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556435">BdaCommitChanges</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563418">KSMETHOD_BDA_START_CHANGES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563403">KSMETHODSETID_BdaChangeSync</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567191">KStrMethodHandler</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20BdaStartChanges function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
