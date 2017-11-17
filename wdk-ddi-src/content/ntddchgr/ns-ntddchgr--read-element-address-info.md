---
UID: NS.ntddchgr._READ_ELEMENT_ADDRESS_INFO
title: READ_ELEMENT_ADDRESS_INFO
author: windows-driver-content
description: This structure is to retrieve changer elements based on a search criterion specified in a call to the ChangerQueryVolumeTags routine.
old-location: storage\read_element_address_info.htm
ms.assetid: 5fc5b38e-8eef-4ba0-9f29-025df55e4525
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddchgr.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: READ_ELEMENT_ADDRESS_INFO
req.alt-loc: ntddchgr.h
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
ms.keywords: READ_ELEMENT_ADDRESS_INFO, READ_ELEMENT_ADDRESS_INFO, *PREAD_ELEMENT_ADDRESS_INFO
req.iface: 
---

# READ_ELEMENT_ADDRESS_INFO structure



## -description
<p>This structure is to retrieve changer elements based on a search criterion specified in a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551440">ChangerQueryVolumeTags</a> routine. </p>


## -syntax

````
typedef struct _READ_ELEMENT_ADDRESS_INFO {
  ULONG                  NumberOfElements;
  CHANGER_ELEMENT_STATUS ElementStatus[1];
} READ_ELEMENT_ADDRESS_INFO, *PREAD_ELEMENT_ADDRESS_INFO;
````


## -struct-fields
<dl>

### -field <b>NumberOfElements</b>

<dd>
<p>Indicates the number of elements that matched the criteria specified by <b>ActionCode</b> and <b>VolumeTemplateID</b> in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551479">CHANGER_SEND_VOLUME_TAG_INFORMATION</a> structure passed to the driver. If no element matches the criteria, this member is zero.</p>
</dd>

### -field <b>ElementStatus</b>

<dd>
<p>Contains an array holding the first <a href="https://msdn.microsoft.com/library/windows/hardware/ff551461">CHANGER_ELEMENT_STATUS</a> structure that matched the criteria in the CHANGER_SEND_VOLUME_TAG_INFORMATION structure passed to the driver. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddchgr.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551479">CHANGER_SEND_VOLUME_TAG_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554979">GET_CHANGER_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551461">CHANGER_ELEMENT_STATUS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551440">ChangerQueryVolumeTags</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20READ_ELEMENT_ADDRESS_INFO structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
