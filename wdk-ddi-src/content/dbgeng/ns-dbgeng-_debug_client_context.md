---
UID: NS.DBGENG._DEBUG_CLIENT_CONTEXT
title: _DEBUG_CLIENT_CONTEXT
author: windows-driver-content
description: Contains a debug client constant to provide to the IDebugClient7::SetClientContext method.
old-location: debugger\debug_client_context.htm
old-project: Debugger
ms.assetid: 69CE0535-3ADD-481C-A016-695A7303BBA5
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _DEBUG_CLIENT_CONTEXT, PDEBUG_CLIENT_CONTEXT, *PDEBUG_CLIENT_CONTEXT, DEBUG_CLIENT_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_CLIENT_CONTEXT
req.alt-loc: DbgEng.h
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

# _DEBUG_CLIENT_CONTEXT structure



## -description
Contains a debug client constant to provide to the <a href="debugger.idebugclient7_setclientcontext">IDebugClient7::SetClientContext</a>  method. 



## -syntax

````
typedef struct _DEBUG_CLIENT_CONTEXT {
  UINT cbSize;
  UINT eClient;
} DEBUG_CLIENT_CONTEXT, *PDEBUG_CLIENT_CONTEXT;
````


## -struct-fields

### -field cbSize

A size value.


### -field eClient

A client value.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>DbgEng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="debugger.idebugclient7_setclientcontext">IDebugClient7::SetClientContext</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20DEBUG_CLIENT_CONTEXT structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

