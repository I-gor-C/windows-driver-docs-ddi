---
UID: NS.NTIFS._SECURITY_DESCRIPTOR
title: _SECURITY_DESCRIPTOR
author: windows-driver-content
description: The SECURITY_DESCRIPTOR structure specifies the security information that is associated with an object. For more information, see the reference page for SECURITY_DESCRIPTOR in the Installable File System documentation.
old-location: kernel\security_descriptor.htm
old-project: kernel
ms.assetid: 0af0685c-d3a3-4c76-8fca-fb38f60411bf
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _SECURITY_DESCRIPTOR, *PISECURITY_DESCRIPTOR, SECURITY_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SECURITY_DESCRIPTOR
req.alt-loc: Wdm.h
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
---

# _SECURITY_DESCRIPTOR structure



## -description
The <b>SECURITY_DESCRIPTOR</b> structure specifies the security information that is associated with an object. For more information, see the reference page for <a href="ifsk.security_descriptor">SECURITY_DESCRIPTOR</a> in the Installable File System documentation.


## -struct-fields


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.obgetobjectsecurity">ObGetObjectSecurity</a>
</dt>
<dt>
<a href="kernel.obreleaseobjectsecurity">ObReleaseObjectSecurity</a>
</dt>
<dt>
<a href="kernel.rtlcreatesecuritydescriptor">RtlCreateSecurityDescriptor</a>
</dt>
<dt>
<a href="kernel.rtllengthsecuritydescriptor">RtlLengthSecurityDescriptor</a>
</dt>
<dt>
<a href="kernel.rtlsetdaclsecuritydescriptor">RtlSetDaclSecurityDescriptor</a>
</dt>
<dt>
<a href="kernel.rtlvalidsecuritydescriptor">RtlValidSecurityDescriptor</a>
</dt>
<dt>
<a href="kernel.seaccesscheck">SeAccessCheck</a>
</dt>
<dt>
<a href="kernel.seassignsecurity">SeAssignSecurity</a>
</dt>
<dt>
<a href="kernel.sedeassignsecurity">SeDeassignSecurity</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20SECURITY_DESCRIPTOR structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
