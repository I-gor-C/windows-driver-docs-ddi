---
UID: NC:wdm.ETWENABLECALLBACK
title: ETWENABLECALLBACK
author: windows-driver-content
description: The EtwEnableCallback function is an optional driver-supplied callback function that is used to receive enable or disable notifications.
old-location: devtest\etwenablecallback.htm
old-project: devtest
ms.assetid: 5953a3ae-b130-42fd-9dc8-974d15c6dfc5
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: devtest.etwenablecallback, EtwEnableCallback callback function [Driver Development Tools], EtwEnableCallback, PETWENABLECALLBACK, PETWENABLECALLBACK, wdm/EtwEnableCallback, etw_km_6405d4d5-382c-4950-9b91-0cb224a3d069.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	wdm.h
apiname:
-	EtwEnableCallback
product: Windows
targetos: Windows
req.typenames: "*PWDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME"
req.product: Windows 10 or later.
---


# ETWENABLECALLBACK function
The <b>EtwEnableCallback</b> function is an optional driver-supplied callback function that is used to receive enable or disable notifications.

## Syntax

```
ETWENABLECALLBACK Etwenablecallback;

_IRQL_requires_same_ VOID Etwenablecallback(
  LPCGUID SourceId,
  ULONG ControlCode,
  UCHAR Level,
  ULONGLONG MatchAnyKeyword,
  ULONGLONG MatchAllKeyword,
  PEVENT_FILTER_DESCRIPTOR FilterData,
  PVOID CallbackContext
)
{...}
```

## Parameters

`SourceId`

The GUID that identifies the session that enabled the provider.

`ControlCode`



`Level`

The level at which the event is enabled. This parameter is a provider-defined value that specifies the verboseness of the events that the provider writes. The provider must write the event if this value is less than or equal to the level value that the event defines. 

This value is passed in the <i>Level</i> parameter of the <a href="http://go.microsoft.com/fwlink/p/?linkid=103398">EnableTraceEx</a> function or the <i>EnableLevel</i> parameter of the <a href="http://go.microsoft.com/fwlink/p/?linkid=103399">EnableTrace</a> function.

`MatchAnyKeyword`

The bitmask of keywords that the provider uses to determine the category of events that it writes. 

This value is passed in the <i>MatchAnyKeyword</i> parameter of the <a href="http://go.microsoft.com/fwlink/p/?linkid=103398">EnableTraceEx</a> function or the <i>EnableFlag</i> parameter of the <a href="http://go.microsoft.com/fwlink/p/?linkid=103399">EnableTrace</a> function. <i>MatchAnyKeyword</i> is a 64-bit value and is basically an extended version of the 32-bit <i>EnableFlag</i>.

`MatchAllKeyword`

This bitmask additionally restricts the category of events that the provider writes. 

This value is passed in the <i>MatchAllKeywords</i> parameter of the <b>EnableTraceEx</b> function.

`FilterData`

The provider-defined data. This parameter is optional. The provider determines the layout of the data and its purpose. For example, the provider can use this data to additionally filter the events that it writes or use it to perform some calculations before writing the events. For detailed information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545684">Event Filter Descriptor</a>.

`CallbackContext`

The context of the callback function that is defined when the provider called <a href="..\wdm\nf-wdm-etwregister.md">EtwRegister</a> to register itself. This parameter is optional.


## Return Value

None

## Remarks

Use the EtwRegister function to specify a pointer to the <b>EtwEnableCallback </b>function.

Use the <i>FilterData</i> parameter of the callback function to supply the provider with sophisticated filtering abilities. The <b>EtwEnableCallback </b>function does not replace the enable-status function calls (<b>EtwEventEnabled</b> and <b>EtwProviderEnabled</b>). However, it serves as a supplement to them. However, unless your level and keywords are currently enabled, the event will not be written, regardless of the <i>FilterData</i> that the callback function provides.

Callers of <b>EtwEnableCallback</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of Windows.  |
| **Target Platform** | Desktop |
| **Header** | wdm.h (include Wdm.h, Ntddk.h) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="http://go.microsoft.com/fwlink/p/?linkid=103398">EnableTraceEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545684">Event Filter Descriptor</a>



<a href="..\wdm\nf-wdm-etwproviderenabled.md">EtwProviderEnabled</a>



<a href="..\wdm\nf-wdm-etweventenabled.md">EtwEventEnabled</a>



<a href="..\wdm\nf-wdm-etwregister.md">EtwRegister</a>



<a href="http://go.microsoft.com/fwlink/p/?linkid=103399">EnableTrace</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [devtest\devtest]:%20PETWENABLECALLBACK callback function%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>