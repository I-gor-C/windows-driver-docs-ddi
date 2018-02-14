---
UID: NS:wdm._CLFS_MGMT_POLICY
title: "_CLFS_MGMT_POLICY"
author: windows-driver-content
description: The CLFS_MGMT_POLICY structure holds a description of a policy for managing a CLFS log.
old-location: kernel\clfs_mgmt_policy.htm
old-project: kernel
ms.assetid: 6765ced9-e21f-4bd9-bb2b-45df1d6dba75
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: CLFS_MGMT_POLICY, kernel.clfs_mgmt_policy, CLFS_MGMT_POLICY structure [Kernel-Mode Driver Architecture], PCLFS_MGMT_POLICY structure pointer [Kernel-Mode Driver Architecture], wdm/PCLFS_MGMT_POLICY, *PCLFS_MGMT_POLICY, kstruct_a_12bfc6be-5318-49df-b74a-251c40c0b916.xml, wdm/CLFS_MGMT_POLICY, _CLFS_MGMT_POLICY, PCLFS_MGMT_POLICY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
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
req.irql: PASSIVE_LEVEL (see Remarks section)
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Wdm.h
apiname:
-	CLFS_MGMT_POLICY
product: Windows
targetos: Windows
req.typenames: CLFS_MGMT_POLICY, *PCLFS_MGMT_POLICY
req.product: Windows 10 or later.
---

# _CLFS_MGMT_POLICY structure
The <b>CLFS_MGMT_POLICY</b> structure holds a description of a policy for managing a CLFS log.

## Syntax
````
typedef struct _CLFS_MGMT_POLICY {
  ULONG                 Version;
  ULONG                 LengthInBytes;
  ULONG                 PolicyFlags;
  CLFS_MGMT_POLICY_TYPE PolicyType;
  union {
    struct {
      ULONG Containers;
    } MaximumSize;
    struct {
      ULONG Containers;
    } MinimumSize;
    struct {
      ULONG SizeInBytes;
    } NewContainerSize;
    struct {
      ULONG AbsoluteGrowthInContainers;
      ULONG RelativeGrowthPercentage;
    } GrowthRate;
    struct {
      ULONG MinimumAvailablePercentage;
      ULONG MinimumAvailableContainers;
    } LogTail;
    struct {
      ULONG Percentage;
    } AutoShrink;
    struct {
      ULONG Enabled;
    } AutoGrow;
    struct {
      USHORT PrefixLengthInBytes;
      WCHAR  PrefixString[1];
    } NewContainerPrefix;
    struct {
      ULONGLONG NextContainerSuffix;
    } NewContainerSuffix;
    struct {
      USHORT ExtensionLengthInBytes;
      WCHAR  ExtensionString[1];
    } NewContainerExtension;
  } PolicyParameters;
} CLFS_MGMT_POLICY, *PCLFS_MGMT_POLICY;
````

## Members


`LengthInBytes`

The length of the <b>CLFS_MGMT_POLICY</b> structure.

`PolicyFlags`

The flags that apply to this instance of the <b>CLFS_MGMT_POLICY</b> structure. The only flag that has been implemented for this release is <b>LOG_POLICY_OVERWRITE</b>, which indicates that when the policy is installed, it will replace the policy of the same type, if such a policy already exists.

`PolicyParameters`

The union that provides the detailed information about this instance of the <b>CLFS_MGMT_POLICY</b> structure.

`PolicyType`

A value of the <a href="..\wdm\ne-wdm-_clfs_mgmt_policy_type.md">CLFS_MGMT_POLICY_TYPE</a> enumeration that supplies the type of this instance of the <b>CLFS_MGMT_POLICY</b> structure.

`Version`

The version of the <b>CLFS_MGMT_POLICY</b> structure. Set this to <b>CLFS_MGMT_POLICY_VERSION</b>.

## Remarks
The way a <b>CLFS_MGMT_POLICY</b> structure is interpreted depends on the type of policy that the structure holds.

You can provide <i>policies</i> that specify how the log will be managed. Each policy is an instance of the <b>CLFS_MGMT_POLICY</b> structure, but the structure is interpreted differently depending on the policy type. CLFS uses the information that you provided in the policies to tailor how it manages the log.

When you create a <b>CLFS_MGMT_POLICY</b> structure whose <b>PolicyType</b> is <b>ClfsMgmtPolicyNewContainerPrefix</b>, be sure to allocate enough space to hold the <b>PolicyParameters.NewContainerPrefix.PrefixString</b> string.

You can only install a policy whose policy type specified in the <b>PolicyType</b> value is <b>ClfsMgmtPolicyNewContainerSize</b> before there are any containers in the log. You can change other policies after the log exists.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="..\wdm\nf-wdm-clfsmgmtquerypolicy.md">ClfsMgmtQueryPolicy</a>



<a href="..\wdm\nf-wdm-clfsmgmtinstallpolicy.md">ClfsMgmtInstallPolicy</a>



<a href="..\wdm\nf-wdm-clfsmgmtremovepolicy.md">ClfsMgmtRemovePolicy</a>



<a href="..\wdm\ne-wdm-_clfs_mgmt_policy_type.md">CLFS_MGMT_POLICY_TYPE</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CLFS_MGMT_POLICY structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>