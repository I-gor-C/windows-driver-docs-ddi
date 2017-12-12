---
UID: NC.pepfx.POFXCALLBACKUPDATEPLATFORMIDLESTATE
title: POFXCALLBACKUPDATEPLATFORMIDLESTATE
author: windows-driver-content
description: The UpdatePlatformIdleState routine is called by the platform extension plug-in (PEP) to update the properties of the specified platform idle state.
old-location: kernel\updateplatformidlestate.htm
old-project: kernel
ms.assetid: A5E3C5DE-DD76-41CF-8A86-37F25A069E1C
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _VPCI_PNP_ID, *PVPCI_PNP_ID, VPCI_PNP_ID
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UpdatePlatformIdleState
req.alt-loc: pepfx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
---

# POFXCALLBACKUPDATEPLATFORMIDLESTATE callback



## -description
The <b>UpdatePlatformIdleState</b> routine is called by the platform extension plug-in (PEP) to update the properties of the specified platform idle state.



## -prototype

````
POFXCALLBACKUPDATEPLATFORMIDLESTATE UpdatePlatformIdleState;

NTSTATUS UpdatePlatformIdleState(
  _In_ POHANDLE                        ProcessorHandle,
  _In_ ULONG                           PlatformState,
  _In_ PPEP_PLATFORM_IDLE_STATE_UPDATE Update
)
{ ... }
````


## -parameters

### -param ProcessorHandle [in]

A POHANDLE value that represents the registration of the processor (as a device) with the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx). The PEP previously received this handle from PoFx during the <a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a> notification that informed the PEP that the processor had been registered with PoFx.


### -param PlatformState [in]

An index that identifies the platform idle state whose properties are to be updated. In response to a previous <a href="kernel.pep_notify_ppm_query_platform_states">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES</a> notification, the PEP specified the number of supported platform idle states. If the PEP specified N platform idle states, valid platform idle state indexes range from 0 to Nâ€“-1. In response to a previous <a href="kernel.pep_notify_ppm_query_platform_state">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE</a> notification, the PEP specified the properties of this platform idle state.


### -param Update [in]

A pointer to a <a href="kernel.pep_platform_idle_state_update">PEP_PLATFORM_IDLE_STATE_UPDATE</a> structure that contains the updated properties of the platform idle state.


## -returns
<b>UpdatePlatformIdleState</b> returns STATUS_SUCCESS if it successfully updates the properties of the platform idle state. Possible error return values include the following status codes.
<dl>
<dt>STATUS_NOT_SUPPORTED</dt>
</dl>The version number in the <b>PEP_PLATFORM_IDLE_STATE_UPDATE</b> structure is not a supported value.
<dl>
<dt>STATUS_NOT_IMPLEMENTED</dt>
</dl>The <b>UpdatePlatformIdleState</b> routine is not implemented for this processor.

 


## -remarks
This routine is implemented by PoFx and is called by the PEP. The <b>UpdatePlatformIdleState</b> member of the <a href="kernel.pep_kernel_information_struct_v3">PEP_KERNEL_INFORMATION_STRUCT_V3</a> structure is a pointer to an <b>UpdatePlatformIdleState</b> routine.

 The PEP must wait until after it has completed all <a href="kernel.pep_notify_ppm_query_platform_state">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE</a> notifications to call the <b>UpdatePlatformIdleState</b> routine.

The <b>UpdatePlatformIdleState</b> routine must be called at IRQL = PASSIVE_LEVEL.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported starting with Windows 10.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a>
</dt>
<dt>
<a href="kernel.pep_kernel_information_struct_v3">PEP_KERNEL_INFORMATION_STRUCT_V3</a>
</dt>
<dt>
<a href="kernel.pep_notify_ppm_query_platform_state">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE</a>
</dt>
<dt>
<a href="kernel.pep_notify_ppm_query_platform_states">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES</a>
</dt>
<dt>
<a href="kernel.pep_platform_idle_state_update">PEP_PLATFORM_IDLE_STATE_UPDATE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20POFXCALLBACKUPDATEPLATFORMIDLESTATE routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

