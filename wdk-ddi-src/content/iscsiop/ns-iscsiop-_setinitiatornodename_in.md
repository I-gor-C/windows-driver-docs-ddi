---
UID: NS.ISCSIOP._SETINITIATORNODENAME_IN
title: _SetInitiatorNodeName_IN
author: windows-driver-content
description: The SetInitiatorNodeName_IN structure holds the input data for the SetInitiatorNodeName method.
old-location: storage\setinitiatornodename_in.htm
old-project: storage
ms.assetid: 58af1872-23bf-44f2-9ef4-271f0ddef5d5
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _SetInitiatorNodeName_IN, PSetInitiatorNodeName_IN, *PSetInitiatorNodeName_IN, SetInitiatorNodeName_IN
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
req.alt-api: SetInitiatorNodeName_IN
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
---

# _SetInitiatorNodeName_IN structure



## -description
The SetInitiatorNodeName_IN structure holds the input data for the <a href="storage.setinitiatornodename">SetInitiatorNodeName</a> method.



## -syntax

````
typedef struct _SetInitiatorNodeName_IN {
  WCHAR CreatedInitiatorName[223 + 1];
} SetInitiatorNodeName_IN, *PSetInitiatorNodeName_IN;
````


## -struct-fields

### -field CreatedInitiatorName

The new initiator name.


## -remarks
It is optional that you implement this class.


## -requirements
<table>
<tr>
<th width="30%">
Header

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
<a href="storage.setinitiatornodename">SetInitiatorNodeName</a>
</dt>
<dt>
<a href="storage.setinitiatornodename_out">SetInitiatorNodeName_OUT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SetInitiatorNodeName_IN structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

