---
UID: NS.FLTKERNEL._FLT_NAME_CONTROL
title: _FLT_NAME_CONTROL
author: windows-driver-content
description: A minifilter that provides file names for the Filter Manager's name cache can use the FLT_NAME_CONTROL structure to manage its name buffers.
old-location: ifsk\flt_name_control.htm
old-project: ifsk
ms.assetid: 0f796ad1-e4b4-4113-b076-ed6c9ea711c9
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: _FLT_NAME_CONTROL, *PFLT_NAME_CONTROL, FLT_NAME_CONTROL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FLT_NAME_CONTROL
req.alt-loc: fltkernel.h
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
---

# _FLT_NAME_CONTROL structure



## -description
A minifilter that provides file names for the Filter Manager's name cache can use the FLT_NAME_CONTROL structure to manage its name buffers. 


## -syntax

````
typedef struct _FLT_NAME_CONTROL {
  UNICODE_STRING Name;
} FLT_NAME_CONTROL, *PFLT_NAME_CONTROL;
````


## -struct-fields

### -field Name


<a href="kernel.unicode_string">UNICODE_STRING</a> structure that contains the file name string. 

## -remarks
Minifilters must not attempt to free or replace the buffer in the <a href="kernel.unicode_string">UNICODE_STRING</a> structure  that the <b>Name</b> member points to directly. Instead, minifilters should call <a href="ifsk.fltcheckandgrownamecontrol">FltCheckAndGrowNameControl</a> to obtain a larger name control buffer. 

## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fltcheckandgrownamecontrol">FltCheckAndGrowNameControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543030">FltGetFileNameFormat</a>
</dt>
<dt>
<a href="ifsk.fltgetfilenameinformation">FltGetFileNameInformation</a>
</dt>
<dt>
<a href="ifsk.fltgetfilenameinformationunsafe">FltGetFileNameInformationUnsafe</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543040">FltGetFileNameQueryMethod</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FLT_NAME_CONTROL structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
