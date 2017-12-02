---
UID: NF.portcls.PcNewInterruptSync
title: PcNewInterruptSync
author: windows-driver-content
description: The PcNewInterruptSync function creates and initializes an interrupt-synchronization object.
old-location: audio\pcnewinterruptsync.htm
old-project: audio
ms.assetid: 2455d09a-608e-4529-9c27-ed760c7da675
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcNewInterruptSync
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: Available starting in  Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcNewInterruptSync
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PcNewInterruptSync function



## -description
<p>The <b>PcNewInterruptSync</b> function creates and initializes an interrupt-synchronization object.</p>


## -syntax

````
NTSTATUS PcNewInterruptSync(
  _Out_    PINTERRUPTSYNC    *OutInterruptSync,
  _In_opt_ PUNKNOWN          OuterUnknown,
  _In_     PRESOURCELIST     ResourceList,
  _In_     ULONG             ResourceIndex,
  _In_     INTERRUPTSYNCMODE Mode
);
````


## -parameters
<dl>

### -param OutInterruptSync [out]

<dd>
<p>Output pointer for the interrupt-synchronization object created by this function. This parameter points to a caller-allocated pointer variable into which the function outputs a reference to the newly created <a href="..\portcls\nn-portcls-iinterruptsync.md">IInterruptSync</a> object. Specify a valid, non-<b>NULL</b> pointer value for this parameter.</p>
</dd>

### -param OuterUnknown [in, optional]

<dd>
<p>Pointer to the <a href="com.iunknown">IUnknown</a> interface of an object that needs to aggregate the object. Unless aggregation is required, set this parameter to <b>NULL</b>.</p>
</dd>

### -param ResourceList [in]

<dd>
<p>Pointer to the <a href="..\portcls\nn-portcls-iresourcelist.md">IResourceList</a> object that was provided to the miniport driver during initialization. The port driver will examine this resource list but will not modify it.</p>
</dd>

### -param ResourceIndex [in]

<dd>
<p>Specifies the index of the interrupt resource in the resource list. If the <a href="audio.iresourcelist_numberofentriesoftype">IResourceList::NumberOfEntriesOfType</a> method returns a count of N for type CmResourceTypeInterrupt, <i>ResourceIndex</i> must be a value in the range 0 to N-1.</p>
</dd>

### -param Mode [in]

<dd>
<p>Specifies the way that multiple ISRs are handled. Set this parameter to one of the INTERRUPTSYNCMODE enumeration values. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p><b>PcNewInterruptSync</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>The <i>Mode</i> parameter is set to one of the INTERRUPTSYNCMODE enumeration values in the following table.</p>

<p><b>InterruptSyncModeNormal</b></p>

<p>Call each ISR in the list until one of them returns STATUS_SUCCESS.</p>

<p><b>InterruptSyncModeAll</b></p>

<p>Call each ISR in the list exactly once, regardless of the return codes of the various ISRs.</p>

<p><b>InterruptSyncModeRepeat</b></p>

<p>Traverse the entire ISR list until a trip through the list occurs in which no ISR in the list returns STATUS_SUCCESS.</p>

<p>For detailed descriptions of these three modes, see <a href="https://msdn.microsoft.com/c9e228e0-6178-442d-a82a-6b14ed67c9d2">Interrupt Sync Objects</a>.</p>

<p>The <i>OutInterruptSync</i>, <i>OuterUnknown</i>, and <i>ResourceList</i> parameters follow the <a href="https://msdn.microsoft.com/e6b19110-37e2-4d23-a528-6393c12ab650">reference-counting conventions for COM objects</a>.</p>

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
<p>Minimum support</p>
</th>
<td width="70%">
<p>Available starting in  Windows 2000. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
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
<a href="..\portcls\nn-portcls-iinterruptsync.md">IInterruptSync</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-iresourcelist.md">IResourceList</a>
</dt>
<dt>
<a href="audio.iresourcelist_numberofentriesoftype">IResourceList::NumberOfEntriesOfType</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcNewInterruptSync function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
