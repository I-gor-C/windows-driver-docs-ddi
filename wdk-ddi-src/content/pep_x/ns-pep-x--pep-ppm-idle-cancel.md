---
UID: NS.pep_x._PEP_PPM_IDLE_CANCEL
title: PEP_PPM_IDLE_CANCEL
author: windows-driver-content
description: The PEP_PPM_IDLE_CANCEL structure indicates why the processor could not enter the previously selected idle state.
old-location: kernel\pep_ppm_idle_cancel.htm
old-project: kernel
ms.assetid: 29B16A23-A3C1-4994-8F72-403BE32ABBD2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_PPM_IDLE_CANCEL, PEP_PPM_IDLE_CANCEL, *PPEP_PPM_IDLE_CANCEL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pep_x.h
req.include-header: Pepfx.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_PPM_IDLE_CANCEL
req.alt-loc: pep_x.h
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

# PEP_PPM_IDLE_CANCEL structure



## -description
<p>The <b>PEP_PPM_IDLE_CANCEL</b> structure indicates why the processor could not enter the previously selected idle state.</p>


## -syntax

````
typedef struct _PEP_PPM_IDLE_CANCEL {
  PEP_PROCESSOR_IDLE_CANCEL_CODE CancelCode;
} PEP_PPM_IDLE_CANCEL, *PPEP_PPM_IDLE_CANCEL;
````


## -struct-fields
<dl>

### -field <b>CancelCode</b>

<dd>
<p>[in] A <a href="kernel.pep_processor_idle_cancel_code">PEP_PROCESSOR_IDLE_CANCEL_CODE</a> enumeration value that indicates why the processor could not enter the idle state selected by the platform extension plug-in (PEP).</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.pep_notify_ppm_idle_cancel">PEP_NOTIFY_PPM_IDLE_CANCEL</a> notification. The <b>CancelCode</b> member of the structure contains an input value that the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx) supplies before this notification is sent.</p>

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
<dt>Pep_x.h (include Pepfx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pep_notify_ppm_idle_cancel">PEP_NOTIFY_PPM_IDLE_CANCEL</a>
</dt>
<dt>
<a href="kernel.pep_processor_idle_cancel_code">PEP_PROCESSOR_IDLE_CANCEL_CODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PPM_IDLE_CANCEL structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
