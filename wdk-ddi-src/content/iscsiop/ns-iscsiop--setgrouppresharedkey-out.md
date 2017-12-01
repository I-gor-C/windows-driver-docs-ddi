---
UID: NS.iscsiop._SetGroupPresharedKey_OUT
title: SetGroupPresharedKey_OUT
author: windows-driver-content
description: The SetGroupPresharedKey_OUT structure holds the output data for the SetGroupPresharedKey method.
old-location: storage\setgrouppresharedkey_out.htm
old-project: storage
ms.assetid: 4ea5e428-783c-4a28-bec5-42106425ee1f
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SetGroupPresharedKey_OUT, SetGroupPresharedKey_OUT, *PSetGroupPresharedKey_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsiop.h
req.include-header: Iscsiop.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetGroupPresharedKey_OUT
req.alt-loc: iscsiop.h
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
req.iface: 
---

# SetGroupPresharedKey_OUT structure



## -description
<p>The SetGroupPresharedKey_OUT structure holds the output data for the <a href="storage.setgrouppresharedkey">SetGroupPresharedKey</a> method.</p>


## -syntax

````
typedef struct _SetGroupPresharedKey_OUT {
  ULONG Status;
} SetGroupPresharedKey_OUT, *PSetGroupPresharedKey_OUT;
````


## -struct-fields
<dl>

### -field <b>Status</b>

<dd>
<p>On output, the status of the <b>SetGroupPresharedKey</b> operation. For a list of status qualifiers, see <a href="storage.iscsi_status_qualifiers">ISCSI_STATUS_QUALIFIERS</a>. </p>
</dd>
</dl>

## -remarks
<p>You must implement this method.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsiop.h (include Iscsiop.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.iscsi_status_qualifiers">ISCSI_STATUS_QUALIFIERS</a>
</dt>
<dt>
<a href="storage.setgrouppresharedkey">SetGroupPresharedKey</a>
</dt>
<dt>
<a href="..\iscsiop\ns-iscsiop--setgrouppresharedkey-in.md">SetGroupPresharedKey_IN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SetGroupPresharedKey_OUT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
