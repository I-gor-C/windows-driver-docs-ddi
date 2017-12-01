---
UID: NF.extsfns.IDebugFailureAnalysis2.GetFailureType
title: IDebugFailureAnalysis2::GetFailureType
author: windows-driver-content
description: The GetFailureType method gets the failure type of a DebugFailureAnalysis object. The failure type indicates whether the code being analyzed was running in kernel mode or user mode.
old-location: debugger\idebugfailureanalysis2_getfailuretype.htm
old-project: debugger
ms.assetid: 3BE85B65-DAE0-41E7-AB24-B5E8E7073E1A
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugFailureAnalysis2, GetFailureType, IDebugFailureAnalysis2::GetFailureType
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: extsfns.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugFailureAnalysis2.GetFailureType
req.alt-loc: extsfns.h
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
req.iface: IDebugFailureAnalysis2
---

# IDebugFailureAnalysis2::GetFailureType method



## -description
<p>The <b>GetFailureType</b> method gets the failure type of a <a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">DebugFailureAnalysis</a> object. The failure type indicates whether the code being analyzed was running in kernel mode or user mode.</p>


## -syntax

````
DEBUG_FAILURE_TYPE GetFailureType();
````


## -parameters


## -returns
<p>This method returns a value in the <a href="..\extsfns\ne-extsfns--debug-failure-type.md">DEBUG_FAILURE_TYPE</a> enumeration.</p>

<p>This method returns a value in the <a href="..\extsfns\ne-extsfns--debug-failure-type.md">DEBUG_FAILURE_TYPE</a> enumeration.</p>

<p>This method returns a value in the <a href="..\extsfns\ne-extsfns--debug-failure-type.md">DEBUG_FAILURE_TYPE</a> enumeration.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Extsfns.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">IDebugFailureAnalysis2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7648F789-85D5-4247-90DD-2EAA43543483">Writing an Analysis Extension Plug-in to Extend !analyze</a>
</dt>
<dt>
<a href="debugger._efn_analyze">_EFN_Analyze</a>
</dt>
<dt>
<a href="debugger.idebugfailureanalysis2_getfailureclass">GetFailureClass</a>
</dt>
<dt><b>GetFailureClass</b></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugFailureAnalysis2::GetFailureType method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
