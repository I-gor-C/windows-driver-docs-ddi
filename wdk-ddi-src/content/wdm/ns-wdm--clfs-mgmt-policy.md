---
UID: NS.wdm._CLFS_MGMT_POLICY
title: CLFS_MGMT_POLICY
author: windows-driver-content
description: The CLFS_MGMT_POLICY structure holds a description of a policy for managing a CLFS log.
old-location: kernel\clfs_mgmt_policy.htm
old-project: kernel
ms.assetid: 6765ced9-e21f-4bd9-bb2b-45df1d6dba75
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: CLFS_MGMT_POLICY, CLFS_MGMT_POLICY, *PCLFS_MGMT_POLICY
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
req.alt-api: CLFS_MGMT_POLICY
req.alt-loc: Wdm.h
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
req.iface: 
req.product: Windows 10 or later.
---

# CLFS_MGMT_POLICY structure



## -description
<p>The <b>CLFS_MGMT_POLICY</b> structure holds a description of a policy for managing a CLFS log.</p>


## -syntax

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


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of the <b>CLFS_MGMT_POLICY</b> structure. Set this to <b>CLFS_MGMT_POLICY_VERSION</b>.</p>
</dd>

### -field <b>LengthInBytes</b>

<dd>
<p>The length of the <b>CLFS_MGMT_POLICY</b> structure.</p>
</dd>

### -field <b>PolicyFlags</b>

<dd>
<p>The flags that apply to this instance of the <b>CLFS_MGMT_POLICY</b> structure. The only flag that has been implemented for this release is <b>LOG_POLICY_OVERWRITE</b>, which indicates that when the policy is installed, it will replace the policy of the same type, if such a policy already exists.</p>
</dd>

### -field <b>PolicyType</b>

<dd>
<p>A value of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541849">CLFS_MGMT_POLICY_TYPE</a> enumeration that supplies the type of this instance of the <b>CLFS_MGMT_POLICY</b> structure.</p>
</dd>

### -field <b>PolicyParameters</b>

<dd>
<p>The union that provides the detailed information about this instance of the <b>CLFS_MGMT_POLICY</b> structure.</p>
<dl>

### -field <b>MaximumSize</b>

<dd>
<p>The structure that provides the detailed information about a policy whose <b>PolicyType</b> is <b>ClfsMgmtPolicyMaximumSize</b>.</p>
<dl>

### -field <b>Containers</b>

<dd>
<p>The maximum number of containers that the log will use.</p>
</dd>
</dl>
</dd>

### -field <b>MinimumSize</b>

<dd>
<p>The structure that provides the detailed information about a policy whose <b>PolicyType</b> is <b>ClfsMgmtPolicyMinimumSize</b>.</p>
<dl>

### -field <b>Containers</b>

<dd>
<p>The minimum number of containers that the log will use.</p>
</dd>
</dl>
</dd>

### -field <b>NewContainerSize</b>

<dd>
<p>The structure that provides the detailed information about a policy whose <b>PolicyType</b> is <b>ClfsMgmtPolicyNewContainerSize</b>.</p>
<dl>

### -field <b>SizeInBytes</b>

<dd>
<p>The size of each of the log's containers.</p>
</dd>
</dl>
</dd>

### -field <b>GrowthRate</b>

<dd>
<p>The structure that provides the detailed information about a policy whose <b>PolicyType</b> is <b>ClfsMgmtPolicyGrowthRate</b>.</p>
<dl>

### -field <b>AbsoluteGrowthInContainers</b>

<dd>
<p>The number of containers that should be added when the size of the log is increased. If the <b>RelativeGrowthPercentage</b> member is nonzero, then <b>AbsoluteGrowthInContainers</b> must be zero.</p>
</dd>

### -field <b>RelativeGrowthPercentage</b>

<dd>
<p>The percentage by which the log's size should increase when the log grows, expressed as a number between zero and 100. For example, if the log consisted of 32 containers and <b>RelativeGrowthPercentage</b> was ten, then, when the log needed to grow, it would grow by three (32 * 10 percent, rounded down to the nearest integer) containers. If the <b>AbsoluteGrowthInContainers</b> member is nonzero, then <b>RelativeGrowthPercentage</b> must be zero.</p>
</dd>
</dl>
</dd>

### -field <b>LogTail</b>

<dd>
<p>The structure that provides the detailed information about a policy whose <b>PolicyType</b> is <b>ClfsMgmtPolicyLogTail</b>.</p>
<dl>

### -field <b>MinimumAvailablePercentage</b>

<dd>
<p>When CLFS management notifies the client to move its log tail, it will specify that the tail be moved to an LSN that leaves at least <b>MinimumAvailablePercentage</b> percent of the log free. If the <b>MinimumAvailableContainers</b> member is nonzero, then <b>MinimumAvailablePercentage</b> must be zero.</p>
</dd>

### -field <b>MinimumAvailableContainers</b>

<dd>
<p>When CLFS management notifies the client to move its log tail, it will specify that the tail be moved to an LSN that leaves at least <b>MinimumAvailableContainers</b> containers free. If the <b>MinimumAvailablePercentage</b> member is nonzero, then <b>MinimumAvailableContainers</b> must be zero.</p>
</dd>
</dl>
</dd>

### -field <b>AutoShrink</b>

<dd>
<p>The structure that provides the detailed information about a policy whose <b>PolicyType</b> is <b>ClfsMgmtPolicyAutoShrink</b>.</p>
<dl>

### -field <b>Percentage</b>

<dd>
<p>When the percentage of free space in the log reaches <b>Percentage</b>, the log will shrink. Percentage is expressed as a number between 0 and 100, so a value of 25 would mean 25 percent.</p>
</dd>
</dl>
</dd>

### -field <b>AutoGrow</b>

<dd>
<p>The structure that provides the detailed information about a policy whose <b>PolicyType</b> is <b>ClfsMgmtPolicyAutoGrow</b>.</p>
<dl>

### -field <b>Enabled</b>

<dd>
<p>A numeric value that determines whether automatic log growth is enabled. Any nonzero value enables automatic growth.</p>
</dd>
</dl>
</dd>

### -field <b>NewContainerPrefix</b>

<dd>
<p>The structure that provides the detailed information about a policy whose <b>PolicyType</b> is <b>ClfsMgmtPolicyNewContainerPrefix</b>.</p>
<dl>

### -field <b>PrefixLengthInBytes</b>

<dd>
<p>The length, in bytes, of the <b>PrefixString</b> member.</p>
</dd>

### -field <b>PrefixString</b>

<dd>
<p>A wide-character string that contains the full path to the directory where the log's containers reside, as well as a prefix that will be used as part of the file name for each container in the log.</p>
</dd>
</dl>
</dd>

### -field <b>NewContainerSuffix</b>

<dd>
<p>The structure that provides the detailed information about a policy whose <b>PolicyType</b> is <b>ClfsMgmtPolicyNewContainerSuffix</b>.</p>
<dl>

### -field <b>NextContainerSuffix</b>

<dd>
<p>The number to use as the suffix of the file name for the next container in the log. To form the file name, the number is converted to a string of decimal digits and appended to the prefix string. The number is incremented for the file name of each subsequent container.</p>
</dd>
</dl>
</dd>

### -field <b>NewContainerExtension</b>

<dd>
<p>The structure that provides the detailed information about a policy whose <b>PolicyType</b> is <b>ClfsMgmtPolicyNewContainerExtension</b>.</p>
<dl>

### -field <b>ExtensionLengthInBytes</b>

<dd>
<p>The length, in bytes, of the <b>ExtensionString</b> member.</p>
</dd>

### -field <b>ExtensionString</b>

<dd>
<p>A wide-character string that contains the extension to the file name for each container in the log. Container file names are built using the format [prefix][suffix][.extension]. An extension is optional. The default extension is the empty string.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The way a <b>CLFS_MGMT_POLICY</b> structure is interpreted depends on the type of policy that the structure holds.</p>

<p>You can provide <i>policies</i> that specify how the log will be managed. Each policy is an instance of the <b>CLFS_MGMT_POLICY</b> structure, but the structure is interpreted differently depending on the policy type. CLFS uses the information that you provided in the policies to tailor how it manages the log.</p>

<p>When you create a <b>CLFS_MGMT_POLICY</b> structure whose <b>PolicyType</b> is <b>ClfsMgmtPolicyNewContainerPrefix</b>, be sure to allocate enough space to hold the <b>PolicyParameters.NewContainerPrefix.PrefixString</b> string.</p>

<p>You can only install a policy whose policy type specified in the <b>PolicyType</b> value is <b>ClfsMgmtPolicyNewContainerSize</b> before there are any containers in the log. You can change other policies after the log exists.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541849">CLFS_MGMT_POLICY_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541634">ClfsMgmtInstallPolicy</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541638">ClfsMgmtQueryPolicy</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541648">ClfsMgmtRemovePolicy</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CLFS_MGMT_POLICY structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
