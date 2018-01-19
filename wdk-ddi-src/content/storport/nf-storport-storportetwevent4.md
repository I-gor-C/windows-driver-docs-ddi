---
UID : NF:storport.StorPortEtwEvent4
title : StorPortEtwEvent4 function
author : windows-driver-content
description : The StorPortEtwEvent4 publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log four general purpose ETW parameters. The ETW parameters are expressed as four name-value pairs.
old-location : storage\storportetwevent4.htm
old-project : storage
ms.assetid : 0F0750A1-142B-4834-85F5-3F5E40EC72F7
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : StorPortEtwEvent4
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : storport.h
req.include-header : Storport.h
req.target-type : Universal
req.target-min-winverclnt : Available in starting with Windows 8.1.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : StorPortEtwEvent4
req.alt-loc : storport.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <= DISPATCH_LEVEL
req.typenames : STOR_SPINLOCK
req.product : Windows 10 or later.
---


# StorPortEtwEvent4 function
The <b>StorPortEtwEvent4</b> publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log four general purpose ETW parameters. The ETW parameters are  expressed as four name-value pairs.

## Syntax

````
ULONG StorPortEtwEvent4(
  _In_     PVOID                     HwDeviceExtension,
  _In_opt_ PSTOR_ADDRESS             Address,
  _In_     ULONG                     EventId,
  _In_     PWSTR                     EventDescription,
  _In_     ULONGLONG                 EventKeywords,
  _In_     STORPORT_ETW_LEVEL        EventLevel,
  _In_     STORPORT_ETW_EVENT_OPCODE EventOpcode,
  _In_opt_ PSCSI_REQUEST_BLOCK       Srb,
  _In_opt_ PWSTR                     Parameter1Name,
  _In_     ULONGLONG                 Parameter1Value,
  _In_opt_ PWSTR                     Parameter2Name,
  _In_     ULONGLONG                 Parameter2Value,
  _In_opt_ PWSTR                     Parameter3Name,
  _In_     ULONGLONG                 Parameter3Value,
  _In_opt_ PWSTR                     Parameter4Name,
  _In_     ULONGLONG                 Parameter4Value
);
````

## Parameters

`HwDeviceExtension`

A pointer to the hardware device extension for the host bus adapter (HBA).

`Address`

The storage unit device address. This parameter is NULL for adapter devices.

`EventId`

A miniport defined identifier for the ETW event.

`EventDescription`

The description text for the event. This text string must be &lt;= STORPORT_ETW_MAX_DESCRIPTION_LENGTH.

`EventKeywords`

Keyword flags for event categorization. Set to 0 if no keyword is desired. The keywords are a bitwise OR combination of the following.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>

`EventLevel`

The event level. This value can indicate the importance or severity of the event. This is one of the following values.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>

`EventOpcode`

The operational nature of the event. This is one of the following values.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>

`Srb`

A pointer to the SRB associated with the logged event. If this parameter contains a valid SRB, this SRB pointer and the associated SRB pointer are logged.

`Parameter1Name`

A description of the of the meaning of <i>Parameter1Value</i>. This parameter name string must be &lt;= STORPORT_ETW_MAX_PARAM_NAME_LENGTH.

`Parameter1Value`

The value for parameter 1.

`Parameter2Name`

A description of the of the meaning of <i>Parameter2Value</i>. This parameter name string must be &lt;= STORPORT_ETW_MAX_PARAM_NAME_LENGTH.

`Parameter2Value`

The value for parameter 2.

`Parameter3Name`

A description of the of the meaning of <i>Parameter3Value</i>. This parameter name string must be &lt;= STORPORT_ETW_MAX_PARAM_NAME_LENGTH.

`Parameter3Value`

The value for parameter 3.

`Parameter4Name`

A description of the of the meaning of <i>Parameter4Value</i>. This parameter name string must be &lt;= STORPORT_ETW_MAX_PARAM_NAME_LENGTH.

`Parameter4Value`

The value for parameter 4.


## Return Value

<b>StorPortEtwEvent4</b> returns one of the following status codes:
<dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl>The event published successfully storage ETW channel.
<dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl>Tracing is not enabled for storage events.
<dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl>The <i>HwDeviceExtension</i> parameter is NULL.

-or-

<i>EventDescription</i> is NULL.

-or-

<i>EventDescription</i> is greater than the maximum name length.

-or-

An ETW parameter name is greater than the maximum name length.

## Remarks

If any parameter is not named, ParameterXName = NULL, the routine will set the corresponding parameter value to 0.

Events generated from StorPort miniport drivers are published to the "Microsoft-Windows-Storage-Storport/Diagnose" ETW channel.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | storport.h (include Storport.h) |
| **Library** |  |
| **IRQL** | <= DISPATCH_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\storport\nf-storport-storportetwevent2.md">StorPortEtwEvent2</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportetwevent8.md">StorPortEtwEvent8</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortEtwEvent4 routine%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>