---
UID: NF.dbgeng.IDebugPlmClient3.SuspendPlmPackageWide
title: IDebugPlmClient3::SuspendPlmPackageWide method
author: windows-driver-content
description: Suspends a Process Lifecycle Management (PLM) package.
old-location: debugger\idebugplmclient3_suspendplmpackagewide.htm
old-project: Debugger
ms.assetid: B887CCD2-0747-483E-A4CF-632471AB19A2
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugPlmClient3, IDebugPlmClient3::SuspendPlmPackageWide, SuspendPlmPackageWide
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugPlmClient3.SuspendPlmPackageWide
req.alt-loc: dbgeng.h
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

# IDebugPlmClient3::SuspendPlmPackageWide method



## -description
Suspends a Process Lifecycle Management (PLM) package.



## -syntax

````
HRESULT SuspendPlmPackageWide(
  [in] ULONG64 Server,
  [in] PCWSTR  PackageFullName
);
````


## -parameters

### -param Server [in]

The server of the package.


### -param PackageFullName [in]

A pointer to the package name.


## -returns
If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugplmclient3.md">IDebugPlmClient3</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugPlmClient3::SuspendPlmPackageWide method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

