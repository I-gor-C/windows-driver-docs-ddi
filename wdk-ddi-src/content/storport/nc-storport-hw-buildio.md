---
UID: NC.storport.HW_BUILDIO
title: HW_BUILDIO
author: windows-driver-content
description: The HwStorBuildIo routine processes the SRB with unsynchronized access to shared system data structures before passing it to HwStorStartIo.
old-location: storage\hwstorbuildio.htm
old-project: storage
ms.assetid: ebbb8289-5996-4d99-98b6-e95fd9dc7ec9
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_DEVICE_UNIQUE_IDENTIFIER, STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HwStorBuildIo
req.alt-loc: Storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL (See Remarks section.)
req.iface: 
req.product: Windows 10 or later.
---

# HW_BUILDIO callback



## -description
<p>The <b>HwStorBuildIo</b> routine processes the SRB with unsynchronized access to shared system data structures before passing it to <a href="https://msdn.microsoft.com/library/windows/hardware/ff557423">HwStorStartIo</a>.</p>


## -prototype

````
HW_BUILDIO HwStorBuildIo;

BOOLEAN HwStorBuildIo(
   IN PVOID               DeviceExtension,
   IN PSCSI_REQUEST_BLOCK Srb 
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceExtension</i> 

<dd>
<p>A pointer to the miniport driver's per HBA storage area. </p>
</dd>

### -param <i>Srb </i> 

<dd>
<p>A pointer to the SCSI request block (SRB) to be processed.</p>
</dd>
</dl>

## -returns
<p><b>HwStorBuildIo</b> returns <b>TRUE</b> to inform the caller that StorPort should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557423">HwStorStartIo</a> routine if StorPort considers the LUN ready to receive I/O. <b>HwStorBuildIo</b> returns <b>FALSE</b> to inform the caller that the SRB should not be passed to <b>HwStorStartIo</b>. In such cases, the miniport driver must complete the SRB by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff567433">StorPortNotification</a> with a notification type of <b>RequestComplete</b>. This can be done in <b>HwStorBuildIo</b> or elsewhere in the miniport driver, as long as the SRB is completed before the timeout that is specified in the <b>TimeOutValue</b> field of the SRB structure.</p>

## -remarks
<p>The name <b>HwStorBuildIo</b> is just a placeholder for the miniport function that is pointed to by the <b>HwBuildIo</b> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559682">HW_INITIALIZATION_DATA</a> structure. The actual prototype of this routine is defined in Storport.h as follows:</p>

<p>The port driver calls the <b>HwStorBuildIo</b> routine at DISPATCH IRQL without holding any spin locks. Because of this, memory allocation using <a href="https://msdn.microsoft.com/library/windows/hardware/ff567031">StorPortAllocatePool</a> and mutual exclusion via <a href="https://msdn.microsoft.com/library/windows/hardware/ff567025">StorPortAcquireSpinLock</a> are allowed in <b>HwStorBuildIo</b>. In a multiprocessor environment, more than one <b>HwStorBuildIo</b> can be active at a time, so the miniport driver is required to synchronize access to system resources, which may be in contention if more than one instance of  <b>HwStorBuildIo</b> is active at any given time.</p>

<p>By completed time-consuming I/O setup activities in <b>HwStorBuildIo</b> instead of in <a href="https://msdn.microsoft.com/library/windows/hardware/ff557423">HwStorStartIo</a>, the miniport driver enables greater I/O concurrency and therefore improves I/O throughput. For highest performance, miniport drivers are expected to do as much preprocessing as possible in <b>HwStorBuildIo</b> so that it can send requests to the HBA via <b>HwStorStartIo</b> in as short amount of time as possible. Preprocessed data and state can be stored in either the <i>DeviceExtension</i> or <i>SrbExtension</i> structures. Only modifications to unique portions of the <i>DeviceExtension</i> must occur since no locks are held. <b>HwStorBuildIo</b> and <b>HwStorStartIo</b> receive the following Srb function types:</p>

<p>SRB_FUNCTION_EXECUTE_SCSI </p>

<p>Sends a CDB to the specified bus/target/lun.</p>

<p>Srb-&gt;DataTransferLength is valid for all Cdbs. </p>

<p>Srb-&gt;DataBuffer is <b>NULL</b> for read and write requests . To access the associated data, either use <a href="https://msdn.microsoft.com/library/windows/hardware/ff567097">StorPortGetScatterGatherList</a> (for Dma transfers) or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567100">StorPortGetSystemAddress</a> (for program controlled I/O ) to get the Scatter Gather list or the virtual address of the buffer.</p>

<p>For other requests, Srb-&gt;Databuffer points to the data that is associated with the Srb.</p>

<p>Srb-&gt;PathId is valid and represents the pathid given to Storport in <a href="https://msdn.microsoft.com/library/windows/hardware/ff567433">StorPortNotification</a> (BusChange). Writers of miniport drivers need to use pathid as an index into a table of busses within the miniport. </p>

<p> Srb-&gt;TargetId and Srb-&gt;Lun are valid.</p>

<p>SRB_FUNCTION_IO_CONTROL </p>

<p>Miniport defined.</p>

<p>Srb-&gt;DataTransferLength and Srb-&gt;DataBuffer are valid if set by the requester.</p>

<p>Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.</p>

<p>SRB_FUNCTION_RESET_LOGICAL_UNIT</p>

<p>Reset the specified logical unit (if the device is capable).</p>

<p>Srb-&gt;DataTransferLength and Srb-&gt;DataBuffer are invalid.</p>

<p>Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.</p>

<p>SRB_FUNCTION_RESET_DEVICE </p>

<p>Reset the specified Scsi Target.</p>

<p>Srb-&gt;DataTransferLength and Srb-&gt;DataBuffer, Srb-&gt;Lun are invalid.</p>

<p>Srb-&gt;PathId and Srb-&gt;TargetId are valid.</p>

<p>SRB_FUNCTION_RESET_BUS </p>

<p>Reset all of the targets on the specified SCSI bus.</p>

<p>Only Srb-&gt;PathId is valid.</p>

<p>SRB_FUNCTION_FLUSH </p>

<p>Only performed by the miniport driver if it sets <b>CachesData</b> == <b>TRUE</b> in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a>. Instructs the miniport driver to flush all cached data.</p>

<p>Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.</p>

<p>SRB_FUNCTION_SHUTDOWN</p>

<p>Only performed by the miniport driver if it sets <b>CachesData</b> == <b>TRUE</b> in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a>. Instructs the miniport driver to flush all cached data preparatory to shut down.</p>

<p>Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.</p>

<p>SRB_FUNCTION_DUMP_POINTERS</p>

<p>This request is sent to a Storport virtual miniport driver that is used to control the disk that holds the crash dump data. The request supplies information needed for the miniport driver to support crash dump and hibernation.</p>

<p>Starting with Windows 8, non-virtual miniport drivers can optionally receive this request</p>

<p>Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.</p>

<p>SRB_FUNCTION_FREE_DUMP_POINTERS</p>

<p>Starting with Windows 8, this request is sent to the miniport to free and resources allocated during the SRB_FUNCTION_DUMP_POINTERS request.</p>

<p>Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.</p>

<p> </p>

<p>Starting in Windows 8, the <i>Srb</i> parameter may point to either <a href="https://msdn.microsoft.com/library/windows/hardware/ff565393">SCSI_REQUEST_BLOCK</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/hh451474">STORAGE_REQUEST_BLOCK</a>. If the function identifier in the <b>Function</b> field of <i>Srb</i> is <b>SRB_FUNCTION_STORAGE_REQUEST_BLOCK</b>, the SRB is a <b>STORAGE_REQUEST_BLOCK</b> request structure.</p>

<p>For more information about what you can and cannot do safely in this miniport driver routine, see <a href="NULL">Unsynchronized HwStorBuildIo Routine</a>. </p>

<p>To define an <b>HwStorBuildIo</b> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p> For example, to define a <b>HwStorBuildIo</b> callback routine that is named <i>MyHwBuildIo</i>, use the <b>HW_BUILDIO</b> type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The <b>HW_BUILDIO</b> function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>HW_BUILDIO</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/40BD11CD-A559-4F90-BF39-4ED2FB800392">Declaring Functions Using Function Role Types for Storport Drivers</a>. For information about _Use_decl_annotations_, see <a href="c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>The name <b>HwStorBuildIo</b> is just a placeholder for the miniport function that is pointed to by the <b>HwBuildIo</b> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559682">HW_INITIALIZATION_DATA</a> structure. The actual prototype of this routine is defined in Storport.h as follows:</p>

<p>The port driver calls the <b>HwStorBuildIo</b> routine at DISPATCH IRQL without holding any spin locks. Because of this, memory allocation using <a href="https://msdn.microsoft.com/library/windows/hardware/ff567031">StorPortAllocatePool</a> and mutual exclusion via <a href="https://msdn.microsoft.com/library/windows/hardware/ff567025">StorPortAcquireSpinLock</a> are allowed in <b>HwStorBuildIo</b>. In a multiprocessor environment, more than one <b>HwStorBuildIo</b> can be active at a time, so the miniport driver is required to synchronize access to system resources, which may be in contention if more than one instance of  <b>HwStorBuildIo</b> is active at any given time.</p>

<p>By completed time-consuming I/O setup activities in <b>HwStorBuildIo</b> instead of in <a href="https://msdn.microsoft.com/library/windows/hardware/ff557423">HwStorStartIo</a>, the miniport driver enables greater I/O concurrency and therefore improves I/O throughput. For highest performance, miniport drivers are expected to do as much preprocessing as possible in <b>HwStorBuildIo</b> so that it can send requests to the HBA via <b>HwStorStartIo</b> in as short amount of time as possible. Preprocessed data and state can be stored in either the <i>DeviceExtension</i> or <i>SrbExtension</i> structures. Only modifications to unique portions of the <i>DeviceExtension</i> must occur since no locks are held. <b>HwStorBuildIo</b> and <b>HwStorStartIo</b> receive the following Srb function types:</p>

<p>SRB_FUNCTION_EXECUTE_SCSI </p>

<p>Sends a CDB to the specified bus/target/lun.</p>

<p>Srb-&gt;DataTransferLength is valid for all Cdbs. </p>

<p>Srb-&gt;DataBuffer is <b>NULL</b> for read and write requests . To access the associated data, either use <a href="https://msdn.microsoft.com/library/windows/hardware/ff567097">StorPortGetScatterGatherList</a> (for Dma transfers) or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567100">StorPortGetSystemAddress</a> (for program controlled I/O ) to get the Scatter Gather list or the virtual address of the buffer.</p>

<p>For other requests, Srb-&gt;Databuffer points to the data that is associated with the Srb.</p>

<p>Srb-&gt;PathId is valid and represents the pathid given to Storport in <a href="https://msdn.microsoft.com/library/windows/hardware/ff567433">StorPortNotification</a> (BusChange). Writers of miniport drivers need to use pathid as an index into a table of busses within the miniport. </p>

<p> Srb-&gt;TargetId and Srb-&gt;Lun are valid.</p>

<p>SRB_FUNCTION_IO_CONTROL </p>

<p>Miniport defined.</p>

<p>Srb-&gt;DataTransferLength and Srb-&gt;DataBuffer are valid if set by the requester.</p>

<p>Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.</p>

<p>SRB_FUNCTION_RESET_LOGICAL_UNIT</p>

<p>Reset the specified logical unit (if the device is capable).</p>

<p>Srb-&gt;DataTransferLength and Srb-&gt;DataBuffer are invalid.</p>

<p>Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.</p>

<p>SRB_FUNCTION_RESET_DEVICE </p>

<p>Reset the specified Scsi Target.</p>

<p>Srb-&gt;DataTransferLength and Srb-&gt;DataBuffer, Srb-&gt;Lun are invalid.</p>

<p>Srb-&gt;PathId and Srb-&gt;TargetId are valid.</p>

<p>SRB_FUNCTION_RESET_BUS </p>

<p>Reset all of the targets on the specified SCSI bus.</p>

<p>Only Srb-&gt;PathId is valid.</p>

<p>SRB_FUNCTION_FLUSH </p>

<p>Only performed by the miniport driver if it sets <b>CachesData</b> == <b>TRUE</b> in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a>. Instructs the miniport driver to flush all cached data.</p>

<p>Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.</p>

<p>SRB_FUNCTION_SHUTDOWN</p>

<p>Only performed by the miniport driver if it sets <b>CachesData</b> == <b>TRUE</b> in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a>. Instructs the miniport driver to flush all cached data preparatory to shut down.</p>

<p>Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.</p>

<p>SRB_FUNCTION_DUMP_POINTERS</p>

<p>This request is sent to a Storport virtual miniport driver that is used to control the disk that holds the crash dump data. The request supplies information needed for the miniport driver to support crash dump and hibernation.</p>

<p>Starting with Windows 8, non-virtual miniport drivers can optionally receive this request</p>

<p>Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.</p>

<p>SRB_FUNCTION_FREE_DUMP_POINTERS</p>

<p>Starting with Windows 8, this request is sent to the miniport to free and resources allocated during the SRB_FUNCTION_DUMP_POINTERS request.</p>

<p>Srb-&gt;PathId, Srb-&gt;TargetId, and Srb-&gt;Lun are all valid.</p>

<p> </p>

<p>Starting in Windows 8, the <i>Srb</i> parameter may point to either <a href="https://msdn.microsoft.com/library/windows/hardware/ff565393">SCSI_REQUEST_BLOCK</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/hh451474">STORAGE_REQUEST_BLOCK</a>. If the function identifier in the <b>Function</b> field of <i>Srb</i> is <b>SRB_FUNCTION_STORAGE_REQUEST_BLOCK</b>, the SRB is a <b>STORAGE_REQUEST_BLOCK</b> request structure.</p>

<p>For more information about what you can and cannot do safely in this miniport driver routine, see <a href="NULL">Unsynchronized HwStorBuildIo Routine</a>. </p>

<p>To define an <b>HwStorBuildIo</b> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p> For example, to define a <b>HwStorBuildIo</b> callback routine that is named <i>MyHwBuildIo</i>, use the <b>HW_BUILDIO</b> type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The <b>HW_BUILDIO</b> function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>HW_BUILDIO</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/40BD11CD-A559-4F90-BF39-4ED2FB800392">Declaring Functions Using Function Role Types for Storport Drivers</a>. For information about _Use_decl_annotations_, see <a href="c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<p>IRQL</p>
</th>
<td width="70%">
<p>DISPATCH_LEVEL (See Remarks section.)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557423">HwStorStartIo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565393">SCSI_REQUEST_BLOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451474">STORAGE_REQUEST_BLOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567433">StorPortNotification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567031">StorPortAllocatePool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567025">StorPortAcquireSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HwStorBuildIo routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
