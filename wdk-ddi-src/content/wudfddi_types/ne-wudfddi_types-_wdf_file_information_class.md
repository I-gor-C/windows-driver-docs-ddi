---
UID : NE:wudfddi_types._WDF_FILE_INFORMATION_CLASS
title : _WDF_FILE_INFORMATION_CLASS
author : windows-driver-content
description : The WDF_FILE_INFORMATION_CLASS enumeration identifies the types of file information that a driver can obtain or set.
old-location : wdf\wdf_file_information_class.htm
old-project : wdf
ms.assetid : d9d6ce1b-8bc1-4ba7-8ee5-3172a780d52c
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _WDF_FILE_INFORMATION_CLASS, WDF_FILE_INFORMATION_CLASS, *PWDF_FILE_INFORMATION_CLASS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : wudfddi_types.h
req.include-header : Wudfddi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 1.9
req.alt-api : WDF_FILE_INFORMATION_CLASS
req.alt-loc : Wudfddi_types.h,Wdffileobject.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : Unavailable in UMDF 2.0 and later.
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : WDF_FILE_INFORMATION_CLASS, *PWDF_FILE_INFORMATION_CLASS
req.product : Windows 10 or later.
---

# _WDF_FILE_INFORMATION_CLASS Enumeration
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>WDF_FILE_INFORMATION_CLASS</b> enumeration identifies the types of file information that a driver can obtain or set.

## Syntax
````
typedef enum _WDF_FILE_INFORMATION_CLASS { 
  WdfFileInformationDirectory                 = 1,
  WdfFileInformationFullDirectory             = 2,
  WdfFileInformationBothDirectory             = 3,
  WdfFileInformationBasic                     = 4,
  WdfFileInformationStandard                  = 5,
  WdfFileInformationInternal                  = 6,
  WdfFileInformationEa                        = 7,
  WdfFileInformationAccess                    = 8,
  WdfFileInformationName                      = 9,
  WdfFileInformationRename                    = 10,
  WdfFileInformationLink                      = 11,
  WdfFileInformationNames                     = 12,
  WdfFileInformationDisposition               = 13,
  WdfFileInformationPosition                  = 14,
  WdfFileInformationFullEa                    = 15,
  WdfFileInformationMode                      = 16,
  WdfFileInformationAlignment                 = 17,
  WdfFileInformationAll                       = 18,
  WdfFileInformationAllocation                = 19,
  WdfFileInformationEndOfFile                 = 20,
  WdfFileInformationAlternateName             = 21,
  WdfFileInformationStream                    = 22,
  WdfFileInformationPipe                      = 23,
  WdfFileInformationPipeLocal                 = 24,
  WdfFileInformationPipeRemote                = 25,
  WdfFileInformationMailslotQuery             = 26,
  WdfFileInformationMailslotSet               = 27,
  WdfFileInformationCompression               = 28,
  WdfFileInformationObjectId                  = 29,
  WdfFileInformationCompletion                = 30,
  WdfFileInformationMoveCluster               = 31,
  WdfFileInformationQuota                     = 32,
  WdfFileInformationReparsePoint              = 33,
  WdfFileInformationNetworkOpen               = 34,
  WdfFileInformationAttributeTag              = 35,
  WdfFileInformationTracking                  = 36,
  WdfFileInformationIdBothDirectory           = 37,
  WdfFileInformationIdFullDirectory           = 38,
  WdfFileInformationValidDataLength           = 39,
  WdfFileInformationShortName                 = 40,
  WdfFileInformationIoCompletionNotification  = 41,
  WdfFileInformationIoStatusBlockRange        = 42,
  WdfFileInformationIoPriorityHint            = 43,
  WdfFileInformationSfioReserve               = 44,
  WdfFileInformationSfioVolume                = 45,
  WdfFileInformationHardLink                  = 46,
  WdfFileInformationProcessIdsUsingFile       = 47,
  WdfFileInformationNormalizedName            = 48,
  WdfFileInformationNetworkPhysicalName       = 49,
  WdfFileInformationIdGlobalTxDirectory       = 50,
  WdfFileInformationIsRemoteDevice            = 51,
  WdfFileInformationAttributeCache            = 52,
  WdfFileInformationMaximum                   = 53
} WDF_FILE_INFORMATION_CLASS, *PWDF_FILE_INFORMATION_CLASS;
````

## Constants

<table>

<tr>
<td>WdfFileInformationAccess</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationAlignment</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationAll</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationAllocation</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationAlternateName</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationAttributeCache</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationAttributeTag</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationBasic</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationBothDirectory</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationCompletion</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationCompression</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationDirectory</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationDisposition</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationEa</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationEndOfFile</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationFullDirectory</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationFullEa</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationHardLink</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationIdBothDirectory</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationIdFullDirectory</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationIdGlobalTxDirectory</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationInternal</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationIoCompletionNotification</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationIoPriorityHint</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationIoStatusBlockRange</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationIsRemoteDevice</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationLink</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationMailslotQuery</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationMailslotSet</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationMaximum</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationMode</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationMoveCluster</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationName</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationNames</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationNetworkOpen</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationNetworkPhysicalName</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationNormalizedName</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationObjectId</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationPipe</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationPipeLocal</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationPipeRemote</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationPosition</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationProcessIdsUsingFile</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationQuota</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationRename</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationReparsePoint</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationSfioReserve</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationSfioVolume</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationShortName</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationStandard</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationStream</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationTracking</td>
<td></td>
</tr>

<tr>
<td>WdfFileInformationValidDataLength</td>
<td></td>
</tr>
</table>

## Remarks

The <b>WDF_FILE_INFORMATION_CLASS</b> enumeration is used as an input value to <a href="https://msdn.microsoft.com/library/windows/hardware/ff558997">IWDFIoRequest2::GetQueryInformationParameters</a> and as an output value from <a href="https://msdn.microsoft.com/library/windows/hardware/ff559009">IWDFIoRequest2::GetSetInformationParameters</a>.

For most values that the <b>WDF_FILE_INFORMATION_CLASS</b> enumeration defines, the wdm.h or ntifs.h header file defines a FILE_XXXX_INFORMATION-named structure that the driver can use when obtaining or setting the file information.

For more information about the enumeration value and associated structures, see the description of the <i>FileInformationClass</i> parameter of <a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a> and <a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** | 1.9 |
| **Header** | wudfddi_types.h (include Wudfddi.h) |

## See Also

<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558997">IWDFIoRequest2::GetQueryInformationParameters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559009">IWDFIoRequest2::GetSetInformationParameters</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_FILE_INFORMATION_CLASS enumeration%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>