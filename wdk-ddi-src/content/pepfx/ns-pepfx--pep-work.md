---
UID: NS.pepfx._PEP_WORK
title: PEP_WORK
author: windows-driver-content
description: The PEP_WORK structure indicates whether the PEP has a work request to submit to the Windows power management framework (PoFx).
old-location: kernel\pep_work.htm
old-project: kernel
ms.assetid: 7C6ACFDD-809E-4E75-8E4D-8A4E0207593E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_WORK, PEP_WORK, *PPEP_WORK
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
req.alt-api: PEP_WORK
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
req.iface: 
---

# PEP_WORK structure



## -description
<p>The <b>PEP_WORK</b> structure indicates whether the PEP has a work request to submit to the Windows <a href="https://msdn.microsoft.com/9F2D8ACD-44D5-46E0-9FC7-1B38B99450FF">power management framework</a> (PoFx).</p>


## -syntax

````
typedef struct _PEP_WORK {
  PPEP_WORK_INFORMATION WorkInformation;
  BOOLEAN               NeedWork;
} PEP_WORK, *PPEP_WORK;
````


## -struct-fields
<dl>

### -field <b>WorkInformation</b>

<dd>
<p>[out] A pointer to a PEP-allocated <a href="..\pepfx\ns-pepfx--pep-work-information.md">PEP_WORK_INFORMATION</a> structure that describes the work that the PEP is requesting. If <b>NeedWork</b> is TRUE, <b>WorkInformation</b> must point to a valid <b>PEP_WORK_INFORMATION</b> structure. If <b>NeedWork</b> is FALSE, <b>WorkInformation</b> must be NULL.</p>
</dd>

### -field <b>NeedWork</b>

<dd>
<p>[out] Whether the PEP has a work request to submit. Set this member to TRUE if the PEP has a work request, or to FALSE if the PEP has no work to request.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.pep_dpm_work">PEP_DPM_WORK</a> notification. Both members of the structure contain values that the PEP writes to the structure in response to this notification.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pep_dpm_work">PEP_DPM_WORK</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-work-information.md">PEP_WORK_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_WORK structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
