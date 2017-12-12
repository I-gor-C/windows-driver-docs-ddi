---
UID: NS.PEPFX._PEP_DEBUGGER_TRANSITION_REQUIREMENTS
title: _PEP_DEBUGGER_TRANSITION_REQUIREMENTS
author: windows-driver-content
description: The PEP_DEBUGGER_TRANSITION_REQUIREMENTS structure indicates the platform idle states for which the debugger device must be turned on.
old-location: kernel\pep_debugger_transition_requirements.htm
old-project: kernel
ms.assetid: 5DF830CA-ECC3-404A-AA5F-3DB487BC85B3
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _PEP_DEBUGGER_TRANSITION_REQUIREMENTS, PEP_DEBUGGER_TRANSITION_REQUIREMENTS, *PPEP_DEBUGGER_TRANSITION_REQUIREMENTS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_DEBUGGER_TRANSITION_REQUIREMENTS
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

# _PEP_DEBUGGER_TRANSITION_REQUIREMENTS structure



## -description
The <b>PEP_DEBUGGER_TRANSITION_REQUIREMENTS</b> structure indicates the platform idle states for which the debugger device must be turned on.



## -syntax

````
typedef struct _PEP_DEBUGGER_TRANSITION_REQUIREMENTS {
  PEPHANDLE DeviceHandle;
  ULONG     PlatformStateCount;
  PBOOLEAN  PowerTransitionRequired;
} PEP_DEBUGGER_TRANSITION_REQUIREMENTS, *PPEP_DEBUGGER_TRANSITION_REQUIREMENTS;
````


## -struct-fields

### -field DeviceHandle

[in] A PEPHANDLE value that identifies the debugger device. The platform extension plug-in (PEP) supplied this handle in response to a previous <a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a> notification.


### -field PlatformStateCount

[in] The number of entries in the array pointed to by the <b>PowerTransitionRequired</b> member. This number is the same as the number of supported platform idle states that the PEP specified in response to a previous <a href="kernel.pep_notify_ppm_query_platform_states">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES</a> notification.


### -field PowerTransitionRequired

[in] An output buffer to which the PEP writes a BOOLEAN array that indicates the platform idle states for which power to the debugger device must be turned on. This buffer is allocated by the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx) and is guaranteed to be large enough to contain the number of array elements specified by the <b>PlatformStateCount</b> member. Set an array element to TRUE if the debugger device must be turned on in the corresponding platform idle state. Set to FALSE to indicate that the device is not required to be turned on in this state. If the platform supports N idle states, the array contains N elements, and idle states are numbered 0 to N–1 in the order in which they are represented in the array.


## -remarks
This structure is used by the <a href="kernel.pep_dpm_query_debugger_transition_requirements">PEP_DPM_QUERY_DEBUGGER_TRANSITION_REQUIREMENTS</a> notification. All three members of the structure contain input values that are supplied by PoFx when this notification is sent to the PEP.

During a debugging session, the debugger component that runs on the target computer communicates with the host computer through a debugger device such as a USB host controller, UART, or networking device.


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
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pep_dpm_query_debugger_transition_requirements">PEP_DPM_QUERY_DEBUGGER_TRANSITION_REQUIREMENTS</a>
</dt>
<dt>
<a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a>
</dt>
<dt>
<a href="kernel.pep_notify_ppm_query_platform_states">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_DEBUGGER_TRANSITION_REQUIREMENTS structure%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

