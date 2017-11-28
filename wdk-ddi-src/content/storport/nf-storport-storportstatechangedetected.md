---
UID: NF.storport.StorPortStateChangeDetected
title: StorPortStateChangeDetected
author: windows-driver-content
description: Notifies the Storport port driver of a state change for a logical unit number (LUN), host bus adapter (HBA) port, or target device.
old-location: storage\storportstatechangedetected.htm
old-project: storage
ms.assetid: 3E5E9C4E-5B82-4656-BDF2-23A9A8D40ADF
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortStateChangeDetected
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortStateChangeDetected
req.alt-loc: storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any
req.iface: 
req.product: Windows 10 or later.
---

# StorPortStateChangeDetected function



## -description
<p>Notifies the Storport port driver of a state change for a logical unit number (LUN), host bus adapter (HBA) port, or target device.</p>


## -syntax

````
ULONG StorPortStateChangeDetected(
  _In_     PVOID            HwDeviceExtension,
  _In_     ULONG            ChangedEntity,
  _In_     PSTOR_ADDRESS    Address,
  _In_     ULONG            Attributes,
  _In_opt_ PHW_STATE_CHANGE HwStateChange,
  _In_opt_ ULONG            HwStateChangeContext
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff567108">StorPortInitialize</a>. The port driver frees this memory when it removes the device.</p>
</dd>

### -param <i>ChangedEntity</i> [in]

<dd>
<p>Flags indicating the entities whose state has changed. This is a bitwise <b>OR</b> combination of these values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="STATE_CHANGE_LUN"></a><a id="state_change_lun"></a><dl>

### -param <b>STATE_CHANGE_LUN</b>


### -param 1 (0x1)

</dl>
</td>
<td width="60%">
<p>LUN state has changed.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STATE_CHANGE_TARGET"></a><a id="state_change_target"></a><dl>

### -param <b>STATE_CHANGE_TARGET</b>


### -param 2 (0x2)

</dl>
</td>
<td width="60%">
<p>Target state has changed.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STATE_CHANGE_BUS"></a><a id="state_change_bus"></a><dl>

### -param <b>STATE_CHANGE_BUS</b>


### -param 4 (0x4)

</dl>
</td>
<td width="60%">
<p> Bus or port state has changed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Address</i> [in]

<dd>
<p>The address of the entity with the state change. <i>Address</i> value cannot change until the callback at  <i>HwStateChange</i> is invoked. If <i>Address</i> is allocated in memory, the memory should be freed by the callback routine.</p>
</dd>

### -param <i>Attributes</i> [in]

<dd>
<p>Attributes associated with the entity. These are a bitwise <b>OR</b> combination of the following:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="ATTRIBUTE_VM_PASSTHROUGH_LUN"></a><a id="attribute_vm_passthrough_lun"></a><dl>

### -param <b>ATTRIBUTE_VM_PASSTHROUGH_LUN</b>

</dl>
</td>
<td width="60%">
<p>LUNs are reserved for virtual machine use.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>HwStateChange</i> [in, optional]

<dd>
<p>A pointer to a callback routine supplied by the miniport. If present, the Storport driver will call this routine when the driver is finished processing this state change notification.</p>
</dd>

### -param <i>HwStateChangeContext</i> [in, optional]

<dd>
<p>A miniport-supplied context value that is included when the routine set in <i>HwStateChange</i> is called.</p>
</dd>
</dl>

## -returns
<p>A status value indicating the result of the notification. This can be one of these values:</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The state change notification is scheduled for processing.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The address type or the entity type is invalid.</p><dl>
<dt><b>STOR_STATUS_UNSUCCESSFUL</b></dt>
</dl><p>A prior notification is in process and this one cannot be scheduled.</p>

<p> </p>

## -remarks
<p>A successful call to<b> StorPortStateChangeDetected</b> results in re-enumeration of the changed entity. </p>

<p>Only one state change request can be active at any time. If a miniport needs to make another <b> StorPortStateChangeDetected</b> call, it should provide a <i>HwStateChange</i> callback and make another call to <b> StorPortStateChangeDetected</b> after the callback to <i>HwStateChange</i> occurs. If a miniport wants to indicate multiple state changes at the same time, the miniport can call <b> StorPortStateChangeDetected</b> once, with  changed entities set in <i>ChangedEntity</i> that includes all of the current state changes.</p>

<p>If multiple flags are specified in <i>ChangedEntity</i>, the  flag with greater value will have precedence over lesser ones.</p>

<p>A successful call to<b> StorPortStateChangeDetected</b> results in re-enumeration of the changed entity. </p>

<p>Only one state change request can be active at any time. If a miniport needs to make another <b> StorPortStateChangeDetected</b> call, it should provide a <i>HwStateChange</i> callback and make another call to <b> StorPortStateChangeDetected</b> after the callback to <i>HwStateChange</i> occurs. If a miniport wants to indicate multiple state changes at the same time, the miniport can call <b> StorPortStateChangeDetected</b> once, with  changed entities set in <i>ChangedEntity</i> that includes all of the current state changes.</p>

<p>If multiple flags are specified in <i>ChangedEntity</i>, the  flag with greater value will have precedence over lesser ones.</p>

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
<p>Available in Windows 8 and later versions of Windows.</p>
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
<p>Any</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451310">HwStorStateChange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortStateChangeDetected routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
