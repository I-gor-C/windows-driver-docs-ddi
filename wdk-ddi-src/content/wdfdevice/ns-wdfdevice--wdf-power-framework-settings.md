---
UID: NS.wdfdevice._WDF_POWER_FRAMEWORK_SETTINGS
title: WDF_POWER_FRAMEWORK_SETTINGS
author: windows-driver-content
description: The WDF_POWER_FRAMEWORK_SETTINGS structure describes power management framework (PoFx) settings for single-component devices.
old-location: wdf\wdf_power_framework_settings.htm
ms.assetid: 2512682A-4E1C-453F-8C46-E8979E46B8EF
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WDF_POWER_FRAMEWORK_SETTINGS
req.alt-loc: wdfdevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WDF_POWER_FRAMEWORK_SETTINGS, WDF_POWER_FRAMEWORK_SETTINGS, *PWDF_POWER_FRAMEWORK_SETTINGS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_POWER_FRAMEWORK_SETTINGS structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The 
  <b>WDF_POWER_FRAMEWORK_SETTINGS</b> structure describes power management framework (PoFx) settings for single-component devices.</p>


## -syntax

````
typedef struct _WDF_POWER_FRAMEWORK_SETTINGS {
  ULONG                                         Size;
  PFN_WDFDEVICE_WDM_POST_PO_FX_REGISTER_DEVICE  EvtDeviceWdmPostPoFxRegisterDevice;
  PFN_WDFDEVICE_WDM_PRE_PO_FX_UNREGISTER_DEVICE EvtDeviceWdmPrePoFxUnregisterDevice;
  PPO_FX_COMPONENT                              Component;
  PPO_FX_COMPONENT_ACTIVE_CONDITION_CALLBACK    ComponentActiveConditionCallback;
  PPO_FX_COMPONENT_IDLE_CONDITION_CALLBACK      ComponentIdleConditionCallback;
  PPO_FX_COMPONENT_IDLE_STATE_CALLBACK          ComponentIdleStateCallback;
  PPO_FX_POWER_CONTROL_CALLBACK                 PowerControlCallback;
  PVOID                                         PoFxDeviceContext;
} WDF_POWER_FRAMEWORK_SETTINGS, *PWDF_POWER_FRAMEWORK_SETTINGS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>EvtDeviceWdmPostPoFxRegisterDevice</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/4CE227F5-9ED4-4484-AFBF-44D1260EB99D">EvtDeviceWdmPostPoFxRegisterDevice</a> event callback function, or NULL.</p>
</dd>

### -field <b>EvtDeviceWdmPrePoFxUnregisterDevice</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/D663C47D-C59E-4210-84D8-9773A3003990">EvtDeviceWdmPrePoFxUnregisterDevice</a> event callback function, or NULL.</p>
</dd>

### -field <b>Component</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh439575">PO_FX_COMPONENT</a> structure that describes the only component
     in the single-component device, or NULL. If NULL, KMDF defaults to F0 support only for this component. This structure specifies the number and attributes of the F-states that the component supports, as well as the deepest Fx state from which the component can awaken.</p>
</dd>

### -field <b>ComponentActiveConditionCallback</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh406416">ComponentActiveConditionCallback</a> callback routine, or NULL. The power management framework (PoFx) calls this callback function when a component becomes active. While in the Active condition, the component is guaranteed to be in F0.</p>
</dd>

### -field <b>ComponentIdleConditionCallback</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh406420">ComponentIdleConditionCallback</a> callback function, or NULL. PoFx calls this callback function when a component becomes idle. While in the Idle condition, the component may be in any F-state, including F0.</p>
</dd>

### -field <b>ComponentIdleStateCallback</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh450931">ComponentIdleStateCallback</a> callback function, or NULL. PoFx calls this callback function when the F-state of the component changes.</p>
</dd>

### -field <b>PowerControlCallback</b>

<dd>
<p>A pointer to the client driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439564">PowerControlCallback</a> callback function, or NULL. PoFx calls this routine to pass a request for a power control operation directly to the driver. If your driver does not support any power control codes, set this parameter to NULL.</p>
</dd>

### -field <b>PoFxDeviceContext</b>

<dd>
<p>A context pointer that the framework supplies to  <a href="https://msdn.microsoft.com/library/windows/hardware/hh406416">ComponentActiveConditionCallback</a>, 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh406420">ComponentIdleConditionCallback</a>,  <a href="https://msdn.microsoft.com/library/windows/hardware/hh450931">ComponentIdleStateCallback</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/hh439564">PowerControlCallback</a>.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_POWER_FRAMEWORK_SETTINGS</b> structure is used an input to <a href="https://msdn.microsoft.com/library/windows/hardware/hh451097">WdfDeviceWdmAssignPowerFrameworkSettings</a>.</p>

<p>To initialize its <b>WDF_POWER_FRAMEWORK_SETTINGS</b> structure, your driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/hh406492">WDF_POWER_FRAMEWORK_SETTINGS_INIT</a>.</p>

<p>For more information, see <a href="wdf.supporting_functional_power_states">Supporting Functional Power States</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh406637">Overview of the Power Management Framework</a>.</p>

<p>This structure is not applicable to KMDF client drivers for multiple-component devices.
 </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406492">WDF_POWER_FRAMEWORK_SETTINGS_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451097">WdfDeviceWdmAssignPowerFrameworkSettings</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4CE227F5-9ED4-4484-AFBF-44D1260EB99D">EvtDeviceWdmPostPoFxRegisterDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/D663C47D-C59E-4210-84D8-9773A3003990">EvtDeviceWdmPrePoFxUnregisterDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_POWER_FRAMEWORK_SETTINGS structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
