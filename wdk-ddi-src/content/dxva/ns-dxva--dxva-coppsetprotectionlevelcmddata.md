---
UID: NS.dxva._DXVA_COPPSetProtectionLevelCmdData
title: DXVA_COPPSetProtectionLevelCmdData
author: windows-driver-content
description: The DXVA_COPPSetProtectionLevelCmdData structure describes the protection types and levels to set on the physical connector associated with a COPP DirectX VA device.
old-location: display\dxva_coppsetprotectionlevelcmddata.htm
ms.assetid: d68d6e50-1373-43bc-a22b-dd9db47614c8
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: This structure applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_COPPSetProtectionLevelCmdData
req.alt-loc: dxva.h
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
ms.keywords: DXVA_COPPSetProtectionLevelCmdData, DXVA_COPPSetProtectionLevelCmdData
req.iface: 
---

# DXVA_COPPSetProtectionLevelCmdData structure



## -description
<p>The DXVA_COPPSetProtectionLevelCmdData structure describes the protection types and levels to set on the physical connector associated with a COPP DirectX VA device.</p>


## -syntax

````
typedef struct _DXVA_COPPSetProtectionLevelCmdData {
  ULONG ProtType;
  ULONG ProtLevel;
  ULONG ExtendedInfoChangeMask;
  ULONG ExtendedInfoData;
} DXVA_COPPSetProtectionLevelCmdData;
````


## -struct-fields
<dl>

### -field <b>ProtType</b>

<dd>
<p>Specifies one of the following protection types to set on the physical connector associated with a COPP device:</p>
<ul>
<li>
<p>COPP_ProtectionType_None (0x00)</p>
</li>
<li>
<p>COPP_ProtectionType_HDCP (0x01)</p>
</li>
<li>
<p>COPP_ProtectionType_ACP (0x02)</p>
</li>
<li>
<p>COPP_ProtectionType_CGMSA (0x04)</p>
</li>
</ul>
</dd>

### -field <b>ProtLevel</b>

<dd>
<p>Specifies the protection level to set for the protection type in <b>ProtType</b> or COPP_NoProtectionLevelAvailable (-1) if no protection level is available.</p>
<ul>
<li>For COPP_ProtectionType_ACP, specifies one of the following values from the <b>COPP_ACP_Protection_Level</b> enumerated type:<ul>
<li>COPP_ACP_Level0 or COPP_ACP_LevelMin (0)</li>
<li>COPP_ACP_Level1 (1)</li>
<li>COPP_ACP_Level2 (2)</li>
<li>COPP_ACP_Level3 or COPP_ACP_LevelMax (3)</li>
</ul>
</li>
<li>For COPP_ProtectionType_CGMSA, specifies one of the following values from the <b>COPP_CGMSA_Protection_Level</b> enumerated type:<ul>
<li>COPP_CGMSA_Disabled or COPP_CGMSA_LevelMin (0)</li>
<li>COPP_CGMSA_CopyFreely (1)</li>
<li>COPP_CGMSA_CopyNoMore (2)</li>
<li>COPP_CGMSA_CopyOneGeneration (3)</li>
<li>COPP_CGMSA_CopyNever (4)</li>
<li>COPP_CGMSA_RedistributionControlRequired (0x08)</li>
<li>(COPP_CGMSA_RedistributionControlRequired + COPP_CGMSA_CopyNever) or COPP_CGMSA_LevelMax</li>
</ul>
</li>
<li>For COPP_ProtectionType_HDCP, specifies one of the following values from the <b>COPP_HDCP_Protection_Level</b> enumerated type:<ul>
<li>COPP_HDCP_Level0 or COPP_HDCP_LevelMin (0)</li>
<li>COPP_HDCP_Level1 or COPP_HDCP_LevelMax (1)</li>
</ul>
</li>
</ul>
</dd>

### -field <b>ExtendedInfoChangeMask</b>

<dd>
<p>Specifies a value that indicates the valid bitfields in the following <b>ExtendedInfoData</b> member.</p>
</dd>

### -field <b>ExtendedInfoData</b>

<dd>
<p>Specifies additional 32-bit data for the protection type in <b>ProtType</b>. Not currently used.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxva.h (include Dxva.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539642">COPPCommand</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563141">DXVA_COPPCommand</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_COPPSetProtectionLevelCmdData structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
