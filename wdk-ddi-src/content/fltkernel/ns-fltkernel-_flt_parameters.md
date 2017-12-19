---
UID: NS.FLTKERNEL._FLT_PARAMETERS
title: _FLT_PARAMETERS
author: windows-driver-content
description: The FLT_PARAMETERS union defines the request-type-specific parameters associated with an I/O operation.
old-location: ifsk\flt_parameters.htm
old-project: ifsk
ms.assetid: 62aa20b7-ce5c-4d42-bce2-1d76a98887ed
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _FLT_PARAMETERS, PFLT_PARAMETERS, *PFLT_PARAMETERS, FLT_PARAMETERS
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
req.alt-api: FLT_PARAMETERS
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

# _FLT_PARAMETERS structure



## -description
The FLT_PARAMETERS union defines the request-type-specific parameters associated with an I/O operation. 



## -syntax

````
typedef union _FLT_PARAMETERS {
  ...
} FLT_PARAMETERS, *PFLT_PARAMETERS;
````


## -struct-fields


## -remarks
This structure is stored in the <b>Parameters</b> field of the <a href="ifsk.flt_io_parameter_block">FLT_IO_PARAMETER_BLOCK</a> structure for the operation. (A pointer to the FLT_IO_PARAMETER_BLOCK structure is stored in the <b>Iopb</b> field of the <a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a> structure for the operation.) 


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
<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="ifsk.flt_io_parameter_block">FLT_IO_PARAMETER_BLOCK</a>
</dt>
<dt>
<a href="ifsk.fltsetcallbackdatadirty">FltSetCallbackDataDirty</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FLT_PARAMETERS union%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

