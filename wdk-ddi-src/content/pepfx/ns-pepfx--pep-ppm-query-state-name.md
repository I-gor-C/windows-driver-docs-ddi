---
UID: NS.pepfx._PEP_PPM_QUERY_STATE_NAME
title: PEP_PPM_QUERY_STATE_NAME
author: windows-driver-content
description: The PEP_PPM_QUERY_STATE_NAME structure contains information about a specific coordinated or platform idle state.
old-location: kernel\pep_ppm_query_state_name.htm
old-project: kernel
ms.assetid: CE0C4DAA-0B14-4CC3-B75A-66329A5830E7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_PPM_QUERY_STATE_NAME, PEP_PPM_QUERY_STATE_NAME, *PPEP_PPM_QUERY_STATE_NAME
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
req.alt-api: PEP_PPM_QUERY_STATE_NAME
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

# PEP_PPM_QUERY_STATE_NAME structure



## -description
<p>The <b>PEP_PPM_QUERY_STATE_NAME</b> structure contains information about a specific coordinated or platform idle state. </p>


## -syntax

````
typedef struct _PEP_PPM_QUERY_STATE_NAME {
  ULONG  StateIndex;
  USHORT NameSize;
  PWSTR  Name;
} PEP_PPM_QUERY_STATE_NAME, *PPEP_PPM_QUERY_STATE_NAME;
````


## -struct-fields
<dl>

### -field <b>StateIndex</b>

<dd>
<p>[in] The index of the state that the OS is querying about.</p>
</dd>

### -field <b>NameSize</b>

<dd>
<p>[in/out] If <b>Name</b> is <b>NULL</b>, returns the size of the buffer required to hold <b>Name</b> (including the trailing <b>UNICODE_NULL</b> character), in WCHARs.
If <b>Name</b> is not <b>NULL</b>, supplies the size of the <b>Name</b> buffer, in WCHARs.   
</p>
</dd>

### -field <b>Name</b>

<dd>
<p>[in] A pointer to a buffer to copy the name of the state to, or <b>NULL</b>. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186778">PEP_NOTIFY_PPM_QUERY_COORDINATED_STATE_NAME notification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186786">PEP_NOTIFY_PPM_QUERY_PROCESSOR_STATE_NAME notification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PPM_QUERY_STATE_NAME structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
