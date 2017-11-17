---
UID: NF.storport.StorPortSynchronizeAccess
title: StorPortSynchronizeAccess
author: windows-driver-content
description: The StorPortSynchronizeAccess routine provides synchronized access to a miniport driver's device extension.
old-location: storage\storportsynchronizeaccess.htm
ms.assetid: eece67ed-faff-4166-8fa0-d501df9c1363
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
req.alt-api: StorPortSynchronizeAccess
req.alt-loc: Storport.lib,Storport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: 
ms.keywords: StorPortSynchronizeAccess
req.iface: 
req.product: Windows 10 or later.
---

# StorPortSynchronizeAccess function



## -description
<p>The <b>StorPortSynchronizeAccess</b> routine provides synchronized access to a miniport driver's device extension. </p>


## -syntax

````
STORPORT_API BOOLEAN StorPortSynchronizeAccess(
  _In_     PVOID                     HwDeviceExtension,
  _In_     PSTOR_SYNCHRONIZED_ACCESS SynchronizedAccessRoutine,
  _In_opt_ PVOID                     Context
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff567108">StorPortInitialize</a>. The port driver frees this memory when it removes the device. </p>
</dd>

### -param <i>SynchronizedAccessRoutine</i> [in]

<dd>
<p>Pointer to a caller-supplied routine whose execution is to be synchronized with the execution of the ISR associated with the interrupt objects. For a prototype of this routine, see the Remarks section later in this topic. </p>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>Pointer to a context area to be passed to the caller-supplied callback routine when it is called. </p>
</dd>
</dl>

## -returns
<p>The return value from  <i>SynchronizedAccessRoutine</i>.</p>

## -remarks
<p>Miniport drivers that operate in full-duplex mode, and that access information that is shared between their <a href="https://msdn.microsoft.com/library/windows/hardware/ff557423">HwStorStartIo</a> routine and interrupt-service routine, must use this routine to access the shared data in a synchronized manner. </p>

<p>The miniport driver passes a callback routine to <b>StorPortSynchronizeAccess</b>, and <b>StorPortSynchronizeAccess</b> calls it after guaranteeing exclusive access to sensitive data structures. The miniport driver's callback routine must conform to the following prototype:</p>

<p>where <i>HwDeviceExtension</i> is a pointer to the hardware device extension, and <i>Context</i> is just a pointer to the same context information that the caller supplied when calling <b>StorPortSynchronizeAccess</b>. </p>

<p>For more information, see <a href="NULL">Synchronized Access within Unsynchronized Miniport Driver Routines</a>.</p>

<p>For more information about synchronization routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff553302">KeSynchronizeExecution</a>.</p>

<p>Miniport drivers that operate in full-duplex mode, and that access information that is shared between their <a href="https://msdn.microsoft.com/library/windows/hardware/ff557423">HwStorStartIo</a> routine and interrupt-service routine, must use this routine to access the shared data in a synchronized manner. </p>

<p>The miniport driver passes a callback routine to <b>StorPortSynchronizeAccess</b>, and <b>StorPortSynchronizeAccess</b> calls it after guaranteeing exclusive access to sensitive data structures. The miniport driver's callback routine must conform to the following prototype:</p>

<p>where <i>HwDeviceExtension</i> is a pointer to the hardware device extension, and <i>Context</i> is just a pointer to the same context information that the caller supplied when calling <b>StorPortSynchronizeAccess</b>. </p>

<p>For more information, see <a href="NULL">Synchronized Access within Unsynchronized Miniport Driver Routines</a>.</p>

<p>For more information about synchronization routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff553302">KeSynchronizeExecution</a>.</p>

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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553302">KeSynchronizeExecution</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20StorPortSynchronizeAccess routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
