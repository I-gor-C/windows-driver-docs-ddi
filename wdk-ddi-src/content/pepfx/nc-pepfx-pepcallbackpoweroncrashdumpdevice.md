---
UID: NC.pepfx.PEPCALLBACKPOWERONCRASHDUMPDEVICE
title: PEPCALLBACKPOWERONCRASHDUMPDEVICE
author: windows-driver-content
description: The PowerOnDumpDeviceCallback callback routine turns on the crash-dump device.
old-location: kernel\powerondumpdevicecallback.htm
old-project: kernel
ms.assetid: 83E5D362-BC3C-4480-9904-6ABBB26DAFF2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VPCI_PNP_ID, VPCI_PNP_ID, *PVPCI_PNP_ID
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
req.alt-api: PowerOnDumpDeviceCallback
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
req.irql: Called at HIGH_LEVEL.
req.iface: 
---

# PEPCALLBACKPOWERONCRASHDUMPDEVICE callback



## -description
<p>The <i>PowerOnDumpDeviceCallback</i> callback routine turns on the crash-dump device.</p>


## -prototype

````
PEPCALLBACKPOWERONCRASHDUMPDEVICE PowerOnDumpDeviceCallback;

BOOLEAN PowerOnDumpDeviceCallback(
  _In_ PPEP_CRASHDUMP_INFORMATION CrashdumpInformation
)
{ ... }
````


## -parameters
<dl>

### -param CrashdumpInformation [in]

<dd>
<p>A pointer to a <a href="..\pepfx\ns-pepfx--pep-crashdump-information.md">PEP_CRASHDUMP_INFORMATION</a> structure that contains information about the crash-dump device.</p>
</dd>
</dl>

## -returns
<p>This routine returns TRUE if it succeeds in turning on power to the crash-dump device. Otherwise, it returns FALSE.</p>

## -remarks
<p>This routine is implemented by the platform extension plug-in (PEP). The routine handles requests from the Windows kernel to turn on the crash-dump device so that a crash dump can be saved to disk.</p>

<p>The PEP registers its <i>PowerOnDumpDeviceCallback</i> routine in response to a <a href="kernel.pep_dpm_register_crashdump_device">PEP_DPM_REGISTER_CRASHDUMP_DEVICE</a> notification from the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx).</p>

<p>The <i>PowerOnDumpDeviceCallback</i> routine is called at IRQL = HIGH_LEVEL with interrupts disabled. Thus, this routine cannot use timers, events, or any synchronization primitives other than spin locks.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Called at HIGH_LEVEL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\pepfx\ns-pepfx--pep-crashdump-information.md">PEP_CRASHDUMP_INFORMATION</a>
</dt>
<dt>
<a href="kernel.pep_dpm_register_crashdump_device">PEP_DPM_REGISTER_CRASHDUMP_DEVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PowerOnDumpDeviceCallback routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
