---
UID: NE.dot11wdi.eDiagnoseLevel
title: eDiagnoseLevel
author: windows-driver-content
description: The eDiagnoseLevel enumeration defines the diagnosis levels for adapter hang diagnosis.
old-location: netvista\wdiediagnoselevel.htm
old-project: netvista
ms.assetid: C19C250D-3C8D-4855-A8B3-82E139CE09BB
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: SYNTHVOICEPRIORITY_INSTANCE, SYNTHVOICEPRIORITY_INSTANCE, *PSYNTHVOICEPRIORITY_INSTANCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: eDiagnoseLevel
req.alt-loc: dot11wdi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: ISynthSinkDMus
---

# eDiagnoseLevel enumeration



## -description
<p>The eDiagnoseLevel enumeration defines the diagnosis levels for adapter hang diagnosis.</p>


## -syntax

````
typedef enum _eDiagnoseLevel { 
  DiagnoseLevelNone               = 0,
  DiagnoseLevelHardwareRegisters  = 1,
  DiagnoseLevelFirmwareImageDump  = 2,
  DiagnoseLevelDriverStateDump    = 3
} eDiagnoseLevel;
````


## -enum-fields
<dl>

### -field DiagnoseLevelNone

<dd>
<p>No diagnostic information should be collected.</p>
</dd>

### -field DiagnoseLevelHardwareRegisters

<dd>
<p>Dump the hardware registers. This information is included in the LiveKD dump.</p>
</dd>

### -field DiagnoseLevelFirmwareImageDump

<dd>
<p>Dump the full firmware image and hardware registers. The firmware image should dump to a file.</p>
</dd>

### -field DiagnoseLevelDriverStateDump

<dd>
<p>Dump the driver state, full firmware image, and hardware registers. The driver state and full firmware image should dump to files.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-adapter-hang-diagnose.md">MiniportWdiAdapterHangDiagnose</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20eDiagnoseLevel enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
